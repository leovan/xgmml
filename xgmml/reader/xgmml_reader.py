import networkx as nx

from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from lxml import etree as ET

from xgmml.utils.xml_utils import *


T = TypeVar('T')


class XGMMLReader(Generic[T], ABC):
    def __init__(self, **kwargs):
        pass

    @abstractmethod
    def _networkx_to(self, graph: nx.MultiGraph, **kwargs) -> T:
        raise NotImplementedError()

    def _read_graph(
        self, graph_xml: ET.ElementTree, namespaces: dict, **kwargs
    ) -> nx.MultiGraph:
        graph_directed = graph_xml.xpath('/g:graph/@directed', namespaces=namespaces)
        graph_directed = (
            True
            if graph_directed[0] == '1'
            else False
            if len(graph_directed) == 1
            else False
        )

        return nx.MultiDiGraph() if graph_directed else nx.MultiGraph()

    def _read_node(
        self,
        graph: nx.MultiGraph,
        graph_xml: ET.ElementTree,
        namespaces: dict,
        **kwargs,
    ):
        for node_xml in graph_xml.xpath('/g:graph/g:node', namespaces=namespaces):
            node_id = node_xml.attrib['id']

            node_attributes = {}

            for att_name, att_value in node_xml.attrib.items():
                if att_name in IGNORED_NODE_ATT_ELEMENTS:
                    continue

                node_attributes[att_name] = att_value

            for att_xml in node_xml.xpath('g:att', namespaces=namespaces):
                att_name = first_or_none(att_xml.xpath('@name'))
                att_type = first_or_none(att_xml.xpath('@type'))
                att_value = first_or_none(att_xml.xpath('@value'))

                if att_name is None or att_type is None or att_value is None:
                    continue

                if att_name in IGNORED_NODE_ATT_ELEMENTS:
                    continue

                att_value = get_att_value(att_value, value_type=att_type)

                node_attributes[att_name] = att_value

            graph.add_node(node_id, **node_attributes)

    def _read_edge(
        self,
        graph: nx.MultiGraph,
        graph_xml: ET.ElementTree,
        namespaces: dict,
        **kwargs,
    ):
        for edge_idx, edge_xml in enumerate(
            graph_xml.xpath('/g:graph/g:edge', namespaces=namespaces)
        ):
            source_node_id = edge_xml.attrib['source']
            target_node_id = edge_xml.attrib['target']

            edge_attributes = {}

            for att_name, att_value in edge_xml.attrib.items():
                if att_name in IGNORED_EDGE_ATT_ELEMENTS:
                    continue

                edge_attributes[att_name] = att_value

            for att_xml in edge_xml.xpath('g:att', namespaces=namespaces):
                att_name = first_or_none(att_xml.xpath('@name'))
                att_type = first_or_none(att_xml.xpath('@type'))
                att_value = first_or_none(att_xml.xpath('@value'))

                if att_name is None or att_type is None or att_value is None:
                    continue

                if att_name in IGNORED_EDGE_ATT_ELEMENTS:
                    continue

                att_value = get_att_value(att_value, value_type=att_type)

                edge_attributes[att_name] = att_value

            graph.add_edge(
                source_node_id, target_node_id, key=edge_idx, **edge_attributes
            )

    def read(self, xgmml_path: str, **kwargs) -> T:
        graph_xml = ET.parse(xgmml_path, ET.XMLParser())

        namespaces = {}
        for prefix, uri in NAMESPACES.items():
            if prefix is not None:
                namespaces[prefix] = uri
            else:
                namespaces['g'] = uri

        graph = self._read_graph(graph_xml, namespaces, **kwargs)
        self._read_node(graph, graph_xml, namespaces, **kwargs)
        self._read_edge(graph, graph_xml, namespaces, **kwargs)

        return self._networkx_to(graph, **kwargs)


__all__ = ['XGMMLReader']
