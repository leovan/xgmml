import uuid
import networkx as nx

from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from datetime import datetime
from lxml import etree as ET
from lxml.builder import ElementMaker, E
from lxml.etree import QName

from xgmml.layout.base_layout import Layout
from xgmml.layout.kamada_kawai_layout import KamadaKawaiLayout
from xgmml.utils.xml_utils import *


T = TypeVar('T')


class XGMMLWriter(Generic[T], ABC):
    def __init__(self, **kwargs):
        self._uuid = str(uuid.uuid4())
        self._element_maker = ElementMaker(nsmap=NAMESPACES)

    @abstractmethod
    def _to_networkx(self, graph: T, **kwargs) -> nx.MultiGraph:
        raise NotImplementedError()

    def _create_value(
        self,
        att_name: str,
        att_value: dict,
        source_data=None,
        source_data_dict=None,
        default_value=None,
        **kwargs,
    ):
        kwarg = att_value['kwarg']
        default = att_value['default']
        value = kwargs.get(kwarg, default)
        value_type = att_value['type'] or get_att_value_type(value)

        mapper_kwarg = att_value.get('mapper_kwarg', None)
        key_kwarg = att_value.get('key_kwarg', None)
        mapper_key = kwargs.get(key_kwarg, None)

        if mapper_kwarg is not None and key_kwarg is not None:
            mapper_cls = kwargs.get(mapper_kwarg, att_value.get('default_mapper', None))
            source_value = source_data.get(mapper_key, None)
            source_values = source_data_dict.get(mapper_key, None)

            if (
                mapper_cls is not None
                and source_value is not None
                and source_values is not None
            ):
                mapper = mapper_cls(source_values, **kwargs)
                value = mapper.map(source_value)

        if value is None:
            value = default_value

        return create_att_value(value, value_type=value_type)

    def _create_att_list(
        self,
        atts: dict[str, dict],
        source_data: dict = None,
        source_data_dict: dict[str, list] = None,
        **kwargs,
    ) -> dict[str, str]:
        att_dict = {}

        for att_name, att_value in atts.items():
            value = self._create_value(
                att_name,
                att_value,
                source_data=source_data,
                source_data_dict=source_data_dict,
                **kwargs,
            )

            if value is not None:
                att_dict[att_name] = value

        return att_dict

    def _create_att_xml_list(
        self,
        atts: dict[str, dict],
        source_data: dict = None,
        source_data_dict: dict[str, list] = None,
        **kwargs,
    ) -> list[ET.Element]:
        att_xml_list = []

        for att_name, att_value in atts.items():
            value_type = att_value['type']
            value = self._create_value(
                att_name,
                att_value,
                source_data=source_data,
                source_data_dict=source_data_dict,
                **kwargs,
            )

            if value is not None:
                att_xml_list.append(
                    E.att(create_att_name_value(att_name, value, value_type=value_type))
                )

        return att_xml_list

    def _create_graph_att_xml_list(
        self, graph_layout: Layout, **kwargs
    ) -> list[ET.Element]:
        graph_type = kwargs.get('graph_type', 'N/A')
        graph_description = kwargs.get('graph_description', 'N/A')
        graph_identifier = kwargs.get('graph_identifier', 'N/A')
        graph_title = kwargs.get('graph_label', self._uuid)
        graph_source = kwargs.get('graph_source', 'https://xgmml.leovan.tech')
        graph_format = kwargs.get('graph_format', 'Cytoscape-XGMML')

        att_xml_list = []

        # rdf
        rdf_element = ET.Element(
            QName(NAMESPACES['rdf'], 'RDF'),
        )

        rdf_description_element = ET.SubElement(
            rdf_element,
            QName(NAMESPACES['rdf'], 'Description'),
            {
                QName(NAMESPACES['rdf'], 'about'): 'https://xgmml.leovan.tech',
            },
        )

        rdf_dc_description_element = ET.SubElement(
            rdf_description_element, QName(NAMESPACES['dc'], 'type')
        )
        rdf_dc_description_element.text = graph_type

        rdf_dc_description_element = ET.SubElement(
            rdf_description_element, QName(NAMESPACES['dc'], 'description')
        )
        rdf_dc_description_element.text = graph_description

        rdf_dc_identifier_element = ET.SubElement(
            rdf_description_element, QName(NAMESPACES['dc'], 'identifier')
        )
        rdf_dc_identifier_element.text = graph_identifier

        rdf_dc_date_element = ET.SubElement(
            rdf_description_element, QName(NAMESPACES['dc'], 'date')
        )
        rdf_dc_date_element.text = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        rdf_dc_title_element = ET.SubElement(
            rdf_description_element, QName(NAMESPACES['dc'], 'title')
        )
        rdf_dc_title_element.text = graph_title

        rdf_dc_source_element = ET.SubElement(
            rdf_description_element, QName(NAMESPACES['dc'], 'source')
        )
        rdf_dc_source_element.text = graph_source

        rdf_dc_format_element = ET.SubElement(
            rdf_description_element, QName(NAMESPACES['dc'], 'format')
        )
        rdf_dc_format_element.text = graph_format

        network_metadata = E.att(
            rdf_element,
            {
                'name': 'networkMetadata',
            },
        )
        att_xml_list.append(network_metadata)

        # others
        att_xml_list.extend(
            [
                E.att(create_att_name_value('shared name', graph_title)),
                E.att(create_att_name_value('name', graph_title)),
                E.att(create_att_name_value('selected', '1', value_type='boolean')),
                E.att(create_att_name_value('layoutAlgorithm', graph_layout.name)),
            ]
        )

        return att_xml_list

    def _create_graph_graphics_xml(self, nodes_position: dict, **kwargs) -> ET.Element:
        graph_label = kwargs.get('graph_label', self._uuid)

        nodes_position_x = [position[0] for position in nodes_position.values()]
        nodes_position_x_min = min(nodes_position_x)
        nodes_position_x_max = max(nodes_position_x)
        graph_width = nodes_position_x_max - nodes_position_x_min
        graph_center_x = (nodes_position_x_max - nodes_position_x_min) / 2.0

        nodes_position_y = [position[1] for position in nodes_position.values()]
        nodes_position_y_min = min(nodes_position_y)
        nodes_position_y_max = max(nodes_position_y)
        graph_height = nodes_position_y_max - nodes_position_y_min
        graph_center_y = (nodes_position_y_max - nodes_position_y_min) / 2.0

        att_xml_list = [
            E.att(create_att_name_value('NETWORK_TITLE', graph_label)),
            E.att(create_att_name_value('NETWORK_WIDTH', graph_width)),
            E.att(create_att_name_value('NETWORK_HEIGHT', graph_height)),
            E.att(create_att_name_value('NETWORK_CENTER_X_LOCATION', graph_center_x)),
            E.att(create_att_name_value('NETWORK_CENTER_Y_LOCATION', graph_center_y)),
        ]

        att_xml_list.extend(
            self._create_att_xml_list(GRAPH_GRAPHICS_ATT_ELEMENTS, **kwargs)
        )

        graphics_element = E.graphics(*att_xml_list)

        return graphics_element

    def _create_node_att_xml_list(
        self, node_id, node_data: dict, **kwargs
    ) -> list[ET.Element]:
        att_xml_list = [
            E.att(create_att_name_value('name', node_id)),
            E.att(create_att_name_value('shared name', node_id)),
        ]

        for name, value in node_data.items():
            if name in IGNORED_NODE_ATT_ELEMENTS:
                continue

            value_type = get_att_value_type(value)
            att_xml_list.append(E.att(create_att_name_value(name, value, value_type)))

        return att_xml_list

    def _create_node_graphics_xml(
        self,
        node_data: dict,
        node_data_dict: dict[str, list],
        node_position: tuple[float, float],
        **kwargs,
    ) -> ET.Element:
        graphics_att_xml_list = self._create_att_xml_list(
            NODE_GRAPHICS_ATT_ELEMENTS, node_data, node_data_dict, **kwargs
        )

        return E.graphics(
            *graphics_att_xml_list,
            {
                **self._create_att_list(
                    NODE_GRAPHICS_ATTS, node_data, node_data_dict, **kwargs
                ),
                'x': str(node_position[0]),
                'y': str(node_position[1]),
                'z': '0.0',
            },
        )

    def _create_node_data_dict(
        self,
        graph: nx.MultiGraph,
    ) -> dict[str, list]:
        node_data_dict = {}
        for _, node_data in graph.nodes(data=True):
            for k, v in node_data.items():
                if k not in node_data_dict:
                    node_data_dict[k] = []

                node_data_dict[k].append(v)

        return node_data_dict

    def _create_node_xml_list(
        self,
        graph: nx.MultiGraph,
        nodes_position: dict[str, tuple[float, float]],
        **kwargs,
    ) -> list[ET.Element]:
        node_data_dict = self._create_node_data_dict(graph)
        node_xml_list = []

        for node_id, node_data in graph.nodes(data=True):
            node_position = nodes_position.get(node_id, (0.0, 0.0))

            att_xml_list = self._create_node_att_xml_list(node_id, node_data, **kwargs)
            att_xml_list.extend(
                self._create_att_xml_list(
                    NODE_ATT_ELEMENTS, node_data, node_data_dict, **kwargs
                )
            )

            graphics_xml = self._create_node_graphics_xml(
                node_data, node_data_dict, node_position, **kwargs
            )

            node_xml = E.node(
                *att_xml_list,
                graphics_xml,
                {
                    'id': node_id,
                    'label': self._create_value(
                        'label',
                        NODE_ATTS['label'],
                        node_data,
                        node_data_dict,
                        default_value=node_id,
                        **kwargs,
                    ),
                },
            )

            node_xml_list.append(node_xml)

        return node_xml_list

    def _create_edge_label(
        self, source_node_id, target_node_id, edge_type, edge_data: dict, **kwargs
    ) -> str:
        edge_label_key = kwargs.get('edge_label_key', None)
        edge_label = edge_data.get(edge_label_key, None)

        if edge_label is None:
            edge_label = f'{source_node_id} ({edge_type}) {target_node_id}'

        return edge_label

    def _create_edge_att_xml_list(
        self, source_node_id, target_node_id, edge_data: dict, **kwargs
    ) -> list[ET.Element]:
        edge_type_key = kwargs.get('edge_type_key', None)
        edge_type = edge_data.get(edge_type_key, '-')

        edge_label = self._create_edge_label(
            source_node_id, target_node_id, edge_type, edge_data, **kwargs
        )

        att_xml_list = [
            E.att(create_att_name_value('name', edge_label)),
            E.att(create_att_name_value('shared name', edge_label)),
            E.att(create_att_name_value('interaction', edge_type)),
            E.att(create_att_name_value('shared interaction', edge_type)),
        ]

        for name, value in edge_data.items():
            if name in IGNORED_EDGE_ATT_ELEMENTS:
                continue

            value_type = get_att_value_type(value)
            att_xml_list.append(E.att(create_att_name_value(name, value, value_type)))

        return att_xml_list

    def _create_edge_graphics_xml(
        self, edge_data: dict, edge_data_dict: dict[str, list], **kwargs
    ) -> ET.Element:
        graphics_att_xml_list = []

        graphics_att_xml_list.extend(
            self._create_att_xml_list(
                EDGE_GRAPHICS_ATT_ELEMENTS, edge_data, edge_data_dict, **kwargs
            )
        )

        return E.graphics(
            *graphics_att_xml_list,
            {
                'width': self._create_value(
                    'width',
                    EDGE_GRAPHICS_ATTS['width'],
                    edge_data,
                    edge_data_dict,
                    **kwargs,
                ),
                'fill': self._create_value(
                    'fill',
                    EDGE_GRAPHICS_ATTS['fill'],
                    edge_data,
                    edge_data_dict,
                    **kwargs,
                ),
            },
        )

    def _create_edge_xml_list(self, graph: nx.MultiGraph, **kwargs) -> list[ET.Element]:
        edge_data_dict = {}
        for _, _, edge_data in graph.edges(data=True):
            for k, v in edge_data.items():
                if k not in edge_data_dict:
                    edge_data_dict[k] = []

                edge_data_dict[k].append(v)

        edge_xml_list = []

        for edge_idx, (source_node_id, target_node_id, edge_data) in enumerate(
            graph.edges(data=True)
        ):
            edge_type_key = kwargs.get('edge_type_key', None)
            edge_type = edge_data.get(edge_type_key, '-')

            edge_label = self._create_edge_label(
                source_node_id, target_node_id, edge_type, edge_data, **kwargs
            )

            att_xml_list = self._create_edge_att_xml_list(
                source_node_id, target_node_id, edge_data, **kwargs
            )
            att_xml_list.extend(
                self._create_att_xml_list(
                    EDGE_ATT_ELEMENTS, edge_data, edge_data_dict, **kwargs
                )
            )

            graphics_xml = self._create_edge_graphics_xml(
                edge_data, edge_data_dict, **kwargs
            )

            edge_xml = E.edge(
                *att_xml_list,
                graphics_xml,
                {
                    'id': str(edge_idx),
                    'label': edge_label,
                    'source': source_node_id,
                    'target': target_node_id,
                    QName(NAMESPACES['cy'], 'directed'): get_directed_value(graph),
                },
            )

            edge_xml_list.append(edge_xml)

        return edge_xml_list

    def _calc_nodes_size(
        self,
        graph: nx.MultiGraph,
        **kwargs,
    ) -> dict[str, tuple[float, float]]:
        node_data_dict = self._create_node_data_dict(graph)

        nodes_size = {}

        for node_id, node_data in graph.nodes(data=True):
            height = self._create_value(
                'h',
                NODE_GRAPHICS_ATTS['h'],
                node_data,
                node_data_dict,
                **kwargs,
            )
            width = self._create_value(
                'w',
                NODE_GRAPHICS_ATTS['w'],
                node_data,
                node_data_dict,
                **kwargs,
            )

            nodes_size[node_id] = (float(height), float(width))

        return nodes_size

    def _calc_nodes_position(
        self, graph: nx.MultiGraph, graph_layout: Layout, graph_layout_kwargs, **kwargs
    ) -> dict[str, tuple[float, float]]:
        nodes_size = self._calc_nodes_size(graph, **kwargs)

        return graph_layout.layout(
            graph,
            nodes_size=nodes_size,
            **graph_layout_kwargs,
        )

    def _create_graph_xml(self, graph: nx.MultiGraph, **kwargs) -> ET.Element:
        graph_id = kwargs.get('graph_id', self._uuid)
        graph_label = kwargs.get('graph_label', self._uuid)
        graph_cy_document_version = kwargs.get('graph_cy_document_version', '3.0')

        graph_attributes = {
            'id': graph_id,
            'label': graph_label,
            'directed': get_directed_value(graph),
            QName(NAMESPACES['cy'], 'documentVersion'): graph_cy_document_version,
        }

        graph_layout_cls = kwargs.get('graph_layout', KamadaKawaiLayout)
        graph_layout_kwargs = kwargs.get('graph_layout_kwargs', {})
        graph_layout = graph_layout_cls(**graph_layout_kwargs)
        nodes_position = self._calc_nodes_position(
            graph, graph_layout, graph_layout_kwargs, **kwargs
        )

        graph_xml = self._element_maker.graph(
            *self._create_graph_att_xml_list(graph_layout, **kwargs),
            self._create_graph_graphics_xml(nodes_position, **kwargs),
            *self._create_node_xml_list(graph, nodes_position, **kwargs),
            *self._create_edge_xml_list(graph, **kwargs),
            graph_attributes,
        )

        return graph_xml

    def write(self, graph: T, xgmml_path: str, **kwargs):
        self._uuid = str(uuid.uuid4())

        graph = self._to_networkx(graph, **kwargs)
        graph_xml = self._create_graph_xml(graph, **kwargs)

        with open(xgmml_path, 'w') as f:
            f.write(
                ET.tostring(
                    graph_xml,
                    encoding='utf-8',
                    pretty_print=True,
                    standalone=True,
                    xml_declaration=True,
                ).decode('utf-8')
            )


__all__ = ['XGMMLWriter']
