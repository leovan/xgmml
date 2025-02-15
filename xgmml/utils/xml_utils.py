import networkx as nx

from lxml.etree import QName

from xgmml.style.style_mapper import *


NAMESPACES = {
    'cy': 'http://www.cytoscape.org',
    'dc': 'http://purl.org/dc/elements/1.1/',
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'xlink': 'http://www.w3.org/1999/xlink',
    None: 'http://www.cs.rpi.edu/XGMML',
}


ATT_TYPES = {
    'boolean': {
        'type': 'boolean',
        QName(NAMESPACES['cy'], 'type'): 'Boolean',
    },
    'integer': {
        'type': 'integer',
        QName(NAMESPACES['cy'], 'type'): 'Integer',
    },
    'real': {
        'type': 'real',
        QName(NAMESPACES['cy'], 'type'): 'Double',
    },
    'string': {
        'type': 'string',
        QName(NAMESPACES['cy'], 'type'): 'String',
    },
}


GRAPH_GRAPHICS_ATT_ELEMENTS = {
    'NETWORK_ANNOTATION_SELECTION': {
        'kwarg': 'graph_annotation_selection',
        'default': 'false',
        'type': 'string',
    },
    'NETWORK_BACKGROUND_PAINT': {
        'kwarg': 'graph_background_color',
        'default': '#FFFFFF',
        'type': 'string',
    },
    'NETWORK_CENTER_X_LOCATION': {
        'kwarg': 'graph_center_x_location',
        'default': None,
        'type': 'string',
    },
    'NETWORK_CENTER_Y_LOCATION': {
        'kwarg': 'graph_center_y_location',
        'default': None,
        'type': 'string',
    },
    'NETWORK_CENTER_Z_LOCATION': {
        'kwarg': 'graph_center_z_location',
        'default': '0.0',
        'type': 'string',
    },
    'NETWORK_DEPTH': {
        'kwarg': 'graph_depth',
        'default': '0.0',
        'type': 'string',
    },
    'NETWORK_EDGE_SELECTION': {
        'kwarg': 'graph_edge_selection',
        'default': 'false',
        'type': 'string',
    },
    'NETWORK_FORCE_HIGH_DETAIL': {
        'kwarg': 'graph_force_high_detail',
        'default': 'false',
        'type': 'string',
    },
    'NETWORK_HEIGHT': {
        'kwarg': 'graph_height',
        'default': None,
        'type': 'string',
    },
    'NETWORK_NODE_LABEL_SELECTION': {
        'kwarg': 'graph_node_label_selection',
        'default': 'false',
        'type': 'string',
    },
    'NETWORK_NODE_SELECTION': {
        'kwarg': 'graph_node_selection',
        'default': 'true',
        'type': 'string',
    },
    'NETWORK_SCALE_FACTOR': {
        'kwarg': 'graph_scale_factor',
        'default': '1.0',
        'type': 'string',
    },
    'NETWORK_TITLE': {
        'kwarg': 'graph_label',
        'default': None,
        'type': 'string',
    },
    'NETWORK_WIDTH': {
        'kwarg': 'graph_width',
        'default': None,
        'type': 'string',
    },
}


NODE_ATTS = {
    'label': {
        'kwarg': 'node_label',
        'default': None,
        'type': 'string',
        'key_kwarg': 'node_label_key',
        'mapper_kwarg': 'node_label_mapper',
        'default_mapper': StylePassthroughMapper,
    }
}


NODE_ATT_ELEMENTS = {
    'selected': {
        'kwarg': 'node_selected',
        'default': '0',
        'type': 'boolean',
        'key_kwarg': 'node_selected_key',
        'mapper_kwarg': 'node_selected_mapper',
        'default_mapper': StylePassthroughMapper,
    },
}


NODE_GRAPHICS_ATTS = {
    'type': {
        'kwarg': 'node_shape',
        'default': 'ELLIPSE',
        'type': 'string',
        'key_kwarg': 'node_shape_key',
        'mapper_kwarg': 'node_shape_mapper',
        'default_mapper': StyleNodeShapeDefaultDiscreteMapper,
    },
    'outline': {
        'kwarg': 'node_outline_color',
        'default': '#CCCCCC',
        'type': 'string',
        'key_kwarg': 'node_outline_color_key',
        'mapper_kwarg': 'node_outline_color_mapper',
        'default_mapper': StyleForegroundColorDefaultDiscreteMapper,
    },
    'width': {
        'kwarg': 'node_outline_width',
        'default': '2.0',
        'type': 'string',
    },
    'fill': {
        'kwarg': 'node_fill_color',
        'default': '#FFFFFF',
        'type': 'string',
        'key_kwarg': 'node_fill_color_key',
        'mapper_kwarg': 'node_fill_color_mapper',
        'default_mapper': StyleBackgroundColorDefaultDiscreteMapper,
    },
    'h': {
        'kwarg': 'node_height',
        'default': '40.0',
        'type': 'string',
        'key_kwarg': 'node_height_key',
        'mapper_kwarg': 'node_height_mapper',
        'default_mapper': StyleNodeSizeDefaultContinuousMapper,
    },
    'w': {
        'kwarg': 'node_width',
        'default': '40.0',
        'type': 'string',
        'key_kwarg': 'node_width_key',
        'mapper_kwarg': 'node_width_mapper',
        'default_mapper': StyleNodeSizeDefaultContinuousMapper,
    },
}


NODE_GRAPHICS_ATT_ELEMENTS = {
    'COMPOUND_NODE_PADDING': {
        'kwarg': 'node_padding',
        'default': '10.0',
        'type': 'string',
    },
    'COMPOUND_NODE_SHAPE': {
        'kwarg': 'node_shape',
        'default': 'ELLIPSE',
        'type': 'string',
        'key_kwarg': 'node_shape_key',
        'mapper_kwarg': 'node_shape_mapper',
        'default_mapper': StyleNodeShapeDefaultDiscreteMapper,
    },
    'NODE_BORDER_STROKE': {
        'kwarg': 'node_border_stroke',
        'default': 'SOLID',
        'type': 'string',
    },
    'NODE_BORDER_TRANSPARENCY': {
        'kwarg': 'node_border_transparency',
        'default': '255',
        'type': 'string',
    },
    'NODE_CUSTOMGRAPHICS_1': {
        'kwarg': 'node_custom_graphics_1',
        'default': 'org.cytoscape.cg.model.NullCustomGraphics,0,[ Remove Graphics ],',
        'type': 'string',
    },
    'NODE_CUSTOMGRAPHICS_2': {
        'kwarg': 'node_custom_graphics_2',
        'default': 'org.cytoscape.cg.model.NullCustomGraphics,0,[ Remove Graphics ],',
        'type': 'string',
    },
    'NODE_CUSTOMGRAPHICS_3': {
        'kwarg': 'node_custom_graphics_3',
        'default': 'org.cytoscape.cg.model.NullCustomGraphics,0,[ Remove Graphics ],',
        'type': 'string',
    },
    'NODE_CUSTOMGRAPHICS_4': {
        'kwarg': 'node_custom_graphics_4',
        'default': 'org.cytoscape.cg.model.NullCustomGraphics,0,[ Remove Graphics ],',
        'type': 'string',
    },
    'NODE_CUSTOMGRAPHICS_5': {
        'kwarg': 'node_custom_graphics_5',
        'default': 'org.cytoscape.cg.model.NullCustomGraphics,0,[ Remove Graphics ],',
        'type': 'string',
    },
    'NODE_CUSTOMGRAPHICS_6': {
        'kwarg': 'node_custom_graphics_6',
        'default': 'org.cytoscape.cg.model.NullCustomGraphics,0,[ Remove Graphics ],',
        'type': 'string',
    },
    'NODE_CUSTOMGRAPHICS_7': {
        'kwarg': 'node_custom_graphics_7',
        'default': 'org.cytoscape.cg.model.NullCustomGraphics,0,[ Remove Graphics ],',
        'type': 'string',
    },
    'NODE_CUSTOMGRAPHICS_8': {
        'kwarg': 'node_custom_graphics_8',
        'default': 'org.cytoscape.cg.model.NullCustomGraphics,0,[ Remove Graphics ],',
        'type': 'string',
    },
    'NODE_CUSTOMGRAPHICS_9': {
        'kwarg': 'node_custom_graphics_9',
        'default': 'org.cytoscape.cg.model.NullCustomGraphics,0,[ Remove Graphics ],',
        'type': 'string',
    },
    'NODE_CUSTOMGRAPHICS_POSITION_1': {
        'kwarg': 'node_custom_graphics_position_1',
        'default': 'C,C,c,0.00,0.00',
        'type': 'string',
    },
    'NODE_CUSTOMGRAPHICS_POSITION_2': {
        'kwarg': 'node_custom_graphics_position_2',
        'default': 'C,C,c,0.00,0.00',
        'type': 'string',
    },
    'NODE_CUSTOMGRAPHICS_POSITION_3': {
        'kwarg': 'node_custom_graphics_position_3',
        'default': 'C,C,c,0.00,0.00',
        'type': 'string',
    },
    'NODE_CUSTOMGRAPHICS_POSITION_4': {
        'kwarg': 'node_custom_graphics_position_4',
        'default': 'C,C,c,0.00,0.00',
        'type': 'string',
    },
    'NODE_CUSTOMGRAPHICS_POSITION_5': {
        'kwarg': 'node_custom_graphics_position_5',
        'default': 'C,C,c,0.00,0.00',
        'type': 'string',
    },
    'NODE_CUSTOMGRAPHICS_POSITION_6': {
        'kwarg': 'node_custom_graphics_position_6',
        'default': 'C,C,c,0.00,0.00',
        'type': 'string',
    },
    'NODE_CUSTOMGRAPHICS_POSITION_7': {
        'kwarg': 'node_custom_graphics_position_7',
        'default': 'C,C,c,0.00,0.00',
        'type': 'string',
    },
    'NODE_CUSTOMGRAPHICS_POSITION_8': {
        'kwarg': 'node_custom_graphics_position_8',
        'default': 'C,C,c,0.00,0.00',
        'type': 'string',
    },
    'NODE_CUSTOMGRAPHICS_POSITION_9': {
        'kwarg': 'node_custom_graphics_position_9',
        'default': 'C,C,c,0.00,0.00',
        'type': 'string',
    },
    'NODE_CUSTOMGRAPHICS_SIZE_1': {
        'kwarg': 'node_custom_graphics_size_1',
        'default': '40.0',
        'type': 'string',
    },
    'NODE_CUSTOMGRAPHICS_SIZE_2': {
        'kwarg': 'node_custom_graphics_size_2',
        'default': '40.0',
        'type': 'string',
    },
    'NODE_CUSTOMGRAPHICS_SIZE_3': {
        'kwarg': 'node_custom_graphics_size_3',
        'default': '40.0',
        'type': 'string',
    },
    'NODE_CUSTOMGRAPHICS_SIZE_4': {
        'kwarg': 'node_custom_graphics_size_4',
        'default': '40.0',
        'type': 'string',
    },
    'NODE_CUSTOMGRAPHICS_SIZE_5': {
        'kwarg': 'node_custom_graphics_size_5',
        'default': '40.0',
        'type': 'string',
    },
    'NODE_CUSTOMGRAPHICS_SIZE_6': {
        'kwarg': 'node_custom_graphics_size_6',
        'default': '40.0',
        'type': 'string',
    },
    'NODE_CUSTOMGRAPHICS_SIZE_7': {
        'kwarg': 'node_custom_graphics_size_7',
        'default': '40.0',
        'type': 'string',
    },
    'NODE_CUSTOMGRAPHICS_SIZE_8': {
        'kwarg': 'node_custom_graphics_size_8',
        'default': '40.0',
        'type': 'string',
    },
    'NODE_CUSTOMGRAPHICS_SIZE_9': {
        'kwarg': 'node_custom_graphics_size_9',
        'default': '40.0',
        'type': 'string',
    },
    'NODE_DEPTH': {
        'kwarg': 'node_depth',
        'default': '0.0',
        'type': 'string',
    },
    'NODE_LABEL': {
        'kwarg': 'node_label',
        'default': None,
        'type': 'string',
        'key_kwarg': 'node_label_key',
        'mapper_kwarg': 'node_label_mapper',
        'default_mapper': StylePassthroughMapper,
    },
    'NODE_LABEL_BACKGROUND_COLOR': {
        'kwarg': 'node_label_background_color',
        'default': '#B6B6B6',
        'type': 'string',
    },
    'NODE_LABEL_BACKGROUND_SHAPE': {
        'kwarg': 'node_label_background_shape',
        'default': 'NONE',
        'type': 'string',
    },
    'NODE_LABEL_BACKGROUND_TRANSPARENCY': {
        'kwarg': 'node_label_background_transparency',
        'default': '255',
        'type': 'string',
    },
    'NODE_LABEL_COLOR': {
        'kwarg': 'node_label_color',
        'default': '#333333',
        'type': 'string',
    },
    'NODE_LABEL_FONT_FACE': {
        'kwarg': 'node_label_font_face',
        'default': 'Dialog,plain,12',
        'type': 'string',
    },
    'NODE_LABEL_FONT_SIZE': {
        'kwarg': 'node_label_font_size',
        'default': '10',
        'type': 'string',
        'key_kwarg': 'node_label_font_size_key',
        'mapper_kwarg': 'node_label_font_size_mapper',
        'default_mapper': StyleFontSizeDefaultContinuousMapper,
    },
    'NODE_LABEL_POSITION': {
        'kwarg': 'node_label_position',
        'default': 'C,C,c,0.00,0.00',
        'type': 'string',
    },
    'NODE_LABEL_ROTATION': {
        'kwarg': 'node_label_rotation',
        'default': '0.0',
        'type': 'string',
    },
    'NODE_LABEL_TRANSPARENCY': {
        'kwarg': 'node_label_transparency',
        'default': '255',
        'type': 'string',
    },
    'NODE_LABEL_WIDTH': {
        'kwarg': 'node_label_width',
        'default': '200.0',
        'type': 'string',
    },
    'NODE_NESTED_NETWORK_IMAGE_VISIBLE': {
        'kwarg': 'node_nested_network_image_visible',
        'default': 'true',
        'type': 'string',
    },
    'NODE_SELECTED': {
        'kwarg': 'node_selected',
        'default': 'false',
        'type': 'string',
        'key_kwarg': 'node_selected_key',
        'mapper_kwarg': 'node_selected_mapper',
        'default_mapper': StylePassthroughMapper,
    },
    'NODE_SELECTED_PAINT': {
        'kwarg': 'node_selected_color',
        'default': '#FFFF00',
        'type': 'string',
    },
    'NODE_TOOLTIP': {
        'kwarg': 'node_tooltip',
        'default': '',
        'type': 'string',
        'key_kwarg': 'node_tooltip_key',
        'mapper_kwarg': 'node_tooltip_mapper',
        'default_mapper': StylePassthroughMapper,
    },
    'NODE_TRANSPARENCY': {
        'kwarg': 'node_transparency',
        'default': '255',
        'type': 'string',
    },
    'NODE_VISIBLE': {
        'kwarg': 'node_visible',
        'default': 'true',
        'type': 'string',
        'key_kwarg': 'node_visible_key',
        'mapper_kwarg': 'node_visible_mapper',
        'default_mapper': StylePassthroughMapper,
    },
}


EDGE_ATTS = {}


EDGE_ATT_ELEMENTS = {
    'selected': {
        'kwarg': 'edge_selected',
        'default': 'false',
        'type': 'boolean',
        'key_kwarg': 'edge_selected_key',
        'mapper_kwarg': 'edge_selected_mapper',
        'default_mapper': StylePassthroughMapper,
    },
}


EDGE_GRAPHICS_ATTS = {
    'width': {
        'kwarg': 'edge_width',
        'default': '2.0',
        'type': 'string',
    },
    'fill': {
        'kwarg': 'edge_fill_color',
        'default': '#999999',
        'type': 'string',
        'key_kwarg': 'edge_fill_color_key',
        'mapper_kwarg': 'edge_fill_color_mapper',
        'default_mapper': StyleBackgroundColorDefaultDiscreteMapper,
    },
}


EDGE_GRAPHICS_ATT_ELEMENTS = {
    'EDGE_BEND': {
        'kwarg': 'edge_bend',
        'default': '',
        'type': 'string',
    },
    'EDGE_CURVED': {
        'kwarg': 'edge_curved',
        'default': 'true',
        'type': 'string',
    },
    'EDGE_LABEL': {
        'kwarg': 'edge_label',
        'default': '',
        'type': 'string',
        'key_kwarg': 'edge_label_key',
        'mapper_kwarg': 'edge_label_mapper',
        'default_mapper': StylePassthroughMapper,
    },
    'EDGE_LABEL_AUTOROTATE': {
        'kwarg': 'edge_label_autorotate',
        'default': 'false',
        'type': 'string',
    },
    'EDGE_LABEL_BACKGROUND_COLOR': {
        'kwarg': 'edge_label_background_color',
        'default': '#B6B6B6',
        'type': 'string',
    },
    'EDGE_LABEL_BACKGROUND_SHAPE': {
        'kwarg': 'edge_label_background_shape',
        'default': 'NONE',
        'type': 'string',
    },
    'EDGE_LABEL_BACKGROUND_TRANSPARENCY': {
        'kwarg': 'edge_label_background_transparency',
        'default': '255',
        'type': 'string',
    },
    'EDGE_LABEL_COLOR': {
        'kwarg': 'edge_label_color',
        'default': '#000000',
        'type': 'string',
    },
    'EDGE_LABEL_FONT_FACE': {
        'kwarg': 'edge_label_font_face',
        'default': 'Dialog,plain,10',
        'type': 'string',
    },
    'EDGE_LABEL_FONT_SIZE': {
        'kwarg': 'edge_label_font_size',
        'default': '10',
        'type': 'string',
    },
    'EDGE_LABEL_POSITION': {
        'kwarg': 'edge_label_position',
        'default': 'C,C,c,0.00,0.00',
        'type': 'string',
    },
    'EDGE_LABEL_ROTATION': {
        'kwarg': 'edge_label_rotation',
        'default': '0.0',
        'type': 'string',
    },
    'EDGE_LABEL_TRANSPARENCY': {
        'kwarg': 'edge_label_transparency',
        'default': '255',
        'type': 'string',
    },
    'EDGE_LABEL_WIDTH': {
        'kwarg': 'edge_label_width',
        'default': '200.0',
        'type': 'string',
    },
    'EDGE_LINE_TYPE': {
        'kwarg': 'edge_line_type',
        'default': 'SOLID',
        'type': 'string',
        'key_kwarg': 'edge_line_type_key',
        'mapper_kwarg': 'edge_line_type_mapper',
        'default_mapper': StyleLineTypeDefaultDiscreteMapper,
    },
    'EDGE_SELECTED': {
        'kwarg': 'edge_selected',
        'default': 'false',
        'type': 'string',
        'key_kwarg': 'edge_selected_key',
        'mapper_kwarg': 'edge_selected_mapper',
        'default_mapper': StylePassthroughMapper,
    },
    'EDGE_SOURCE_ARROW_SELECTED_PAINT': {
        'kwarg': 'edge_source_arrow_selected_color',
        'default': '#FFFF00',
        'type': 'string',
    },
    'EDGE_SOURCE_ARROW_SHAPE': {
        'kwarg': 'edge_source_arrow_shape',
        'default': 'NONE',
        'type': 'string',
        'key_kwarg': 'edge_source_arrow_shape_key',
        'mapper_kwarg': 'edge_source_arrow_shape_mapper',
        'default_mapper': StyleArrowShapeDefaultDiscreteMapper,
    },
    'EDGE_SOURCE_ARROW_SIZE': {
        'kwarg': 'edge_source_arrow_size',
        'default': '6.0',
        'type': 'string',
    },
    'EDGE_SOURCE_ARROW_UNSELECTED_PAINT': {
        'kwarg': 'edge_source_arrow_unselected_color',
        'default': '#000000',
        'type': 'string',
    },
    'EDGE_STACKING': {
        'kwarg': 'edge_stacking',
        'default': 'AUTO_BEND',
        'type': 'string',
    },
    'EDGE_STACKING_DENSITY': {
        'kwarg': 'edge_stacking_density',
        'default': '0.5',
        'type': 'string',
    },
    'EDGE_STROKE_SELECTED_PAINT': {
        'kwarg': 'edge_stroke_selected_color',
        'default': '#FF0000',
        'type': 'string',
    },
    'EDGE_TARGET_ARROW_SELECTED_PAINT': {
        'kwarg': 'edge_target_arrow_selected_color',
        'default': '#FFFF00',
        'type': 'string',
    },
    'EDGE_TARGET_ARROW_SHAPE': {
        'kwarg': 'edge_target_arrow_shape',
        'default': 'NONE',
        'type': 'string',
        'key_kwarg': 'edge_target_arrow_shape_key',
        'mapper_kwarg': 'edge_target_arrow_shape_mapper',
        'default_mapper': StyleArrowShapeDefaultDiscreteMapper,
    },
    'EDGE_TARGET_ARROW_SIZE': {
        'kwarg': 'edge_target_arrow_size',
        'default': '6.0',
        'type': 'string',
    },
    'EDGE_TARGET_ARROW_UNSELECTED_PAINT': {
        'kwarg': 'edge_target_arrow_unselected_color',
        'default': '#000000',
        'type': 'string',
    },
    'EDGE_TOOLTIP': {
        'kwarg': 'edge_tooltip',
        'default': '',
        'type': 'string',
        'key_kwarg': 'edge_tooltip_key',
        'mapper_kwarg': 'edge_tooltip_mapper',
        'default_mapper': StylePassthroughMapper,
    },
    'EDGE_TRANSPARENCY': {
        'kwarg': 'edge_transparency',
        'default': '170',
        'type': 'string',
    },
    'EDGE_VISIBLE': {
        'kwarg': 'edge_visible',
        'default': 'true',
        'type': 'string',
        'key_kwarg': 'edge_visible_key',
        'mapper_kwarg': 'edge_visible_mapper',
        'default_mapper': StylePassthroughMapper,
    },
    'EDGE_Z_ORDER': {
        'kwarg': 'edge_z_order',
        'default': '0.0',
        'type': 'string',
    },
}


IGNORED_NODE_ATT_ELEMENTS = [
    'name',
    'selected',
    'shared name',
]


IGNORED_EDGE_ATT_ELEMENTS = {
    'id',
    'interaction',
    'label',
    'name',
    'selected',
    'shared interaction',
    'shared name',
    'source',
    'target',
    str(QName(NAMESPACES['cy'], 'directed')),
}


def get_att_value_type(value: any) -> str:
    if isinstance(value, bool):
        return 'boolean'
    elif isinstance(value, int):
        return 'integer'
    elif isinstance(value, float):
        return 'real'
    else:
        return 'string'


def get_att_value(value, value_type='string'):
    if value_type == 'boolean':
        return bool(int(value))
    elif value_type == 'integer':
        return int(value)
    elif value_type == 'real':
        return float(value)
    else:
        return str(value)


def get_directed_value(graph: nx.MultiGraph) -> str:
    return '1' if graph.is_directed() else '0'


def create_att_value(value, value_type='string'):
    if value is None:
        return None

    if isinstance(value, bool):
        if value_type == 'boolean':
            return str(int(value))
        else:
            return str(value).lower()
    else:
        return str(value)


def create_att_name_value(name, value, value_type='string') -> dict:
    att = {
        'name': name,
    }

    value = create_att_value(value, value_type=value_type)

    if value is not None:
        att['value'] = value

    if value_type in ATT_TYPES:
        att.update(ATT_TYPES[value_type])

    return att


def first_or_none(values):
    return values[0] if len(values) > 0 else None


__all__ = [
    'NAMESPACES',
    'ATT_TYPES',
    'GRAPH_GRAPHICS_ATT_ELEMENTS',
    'NODE_ATTS',
    'NODE_ATT_ELEMENTS',
    'NODE_GRAPHICS_ATTS',
    'NODE_GRAPHICS_ATT_ELEMENTS',
    'EDGE_ATTS',
    'EDGE_ATT_ELEMENTS',
    'EDGE_GRAPHICS_ATTS',
    'EDGE_GRAPHICS_ATT_ELEMENTS',
    'IGNORED_NODE_ATT_ELEMENTS',
    'IGNORED_EDGE_ATT_ELEMENTS',
    'get_att_value_type',
    'get_att_value',
    'get_directed_value',
    'create_att_value',
    'create_att_name_value',
    'first_or_none',
]
