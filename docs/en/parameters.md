---
icon: lucide/variable
---

# Parameters

!!! tip "Tips"

    For details of the style related parameters, please see: <https://manual.cytoscape.org/en/stable/Styles.html>.

## Reader

| Parameter | Type | Default | Description |
| ---------- | ---- | ------ | ----------- |
| xgmml_path | str  |        | XGMML path  |

## Writer

### Graph

| Parameter                  | Type   | Default                                            | Description                                |
| :------------------------- | :----- | :------------------------------------------------- | :----------------- |
| graph_annotation_selection | bool   | False                                              | Whether graph annotation can be selected   |
| graph_background_color     | str    | <span style="background: #FFFFFF;">\#FFFFFF</span> | Graph background color                     |
| graph_center_x_location    | float  | Automatically generated                            | Graph center x-axis location               |
| graph_center_y_location    | float  | Automatically generated                            | Graph center y-axis location               |
| graph_center_z_location    | float  | 0                                                  | Graph center z-axis location               |
| graph_cy_document_version  | str    | 3.0                                                | Cytoscape document version                 |
| graph_depth                | float  | 0                                                  | Graph depth                                |
| graph_description          | str    | N/A                                                | Graph description                          |
| graph_edge_selection       | bool   | False                                              | Whether graph edge can be selected         |
| graph_force_high_detail    | bool   | False                                              | Whether graph is forced to display details |
| graph_format               | str    | Cytoscape-XGMML                                    | Graph format                               |
| graph_height               | float  | Automatically generated                            | Graph height                               |
| graph_id                   | str    | Automatically generated                            | Graph ID                                   |
| graph_identifier           | str    | N/A                                                | Graph identifier                           |
| graph_label                | str    | Automatically generated                            | Graph name                                 |
| graph_layout               | Layout | KamadaKawaiLayout                                  | Graph layout algorithm                     |
| graph_layout_kwargs        | dict   | {}                                                 | Graph layout algorithm parameters          |
| graph_node_label_selection | bool   | False                                              | Whether graph node label can be selected   |
| graph_node_selection       | bool   | True                                               | Whether graph node can be selected         |
| graph_scale_factor         | float  | 1                                                  | Graph scaling factor                       |
| graph_source               | str    | https://xgmml.leovan.tech                          | Graph source                               |
| graph_type                 | str    | N/A                                                | Graph type                                 |
| graph_width                | float  | Auto-Generate                                      | Graph width                                |

### Node

| Parameter                          | Type        | Default                                                      | Description                                |
| ---------------------------------- | ----------- | ------------------------------------------------------------ | ---------------------- |
| node_border_stroke                 | str         | SOLID                                                        | Node stroke type                           |
| node_border_transparency           | int         | 255                                                          | Node stroke transparency                   |
| node_depth                         | float       | 0.0                                                          | Node depth                                 |
| node_fill_color                    | str         | <span style="background: #FFFFFF;">\#FFFFFF</span>           | Node fill color                            |
| node_fill_color_key                | str         |                                                              | Node fill color mapping attribute key      |
| node_fill_color_mapper             | StyleMapper | StyleBackgroundColorDefaultDiscreteMapper                    | Node fill color mapper                     |
| node_height                        | float       | 40.0                                                         | Node height                                |
| node_height_key                    | str         |                                                              | Node height mapping attribute key          |
| node_height_mapper                 | StyleMapper | StyleNodeSizeDefaultContinuousMapper                         | Node height mapper                         |
| node_label                         | str         |                                                              | Node label                                 |
| node_label_key                     | str         |                                                              | Node label mapping attribute key           |
| node_label_mapper                  | str         | StylePassthroughMapper                                       | Node label mapper                          |
| node_label_background_color        | str         | <span style="background: #B6B6B6;">\#B6B6B6</span>           | Node label background color                |
| node_label_background_shape        | str         | NONE                                                         | Node label background shape                |
| node_label_background_transparency | int         | 255                                                          | Node label background transparency         |
| node_label_color                   | str         | <span style="background: #333333; color: #FFFFFF;">\#333333</span> | Node label color                           |
| node_label_font_face               | str         | Dialog,plain,12                                              | Node label font                            |
| node_label_font_size               | int         | 10                                                           | Node label font size                       |
| node_label_font_size_key           | str         |                                                              | Node label font size mapping attribute key |
| node_label_font_size_mapper        | StyleMapper | StyleFontSizeDefaultContinuousMapper                         | Node label font size mapper                |
| node_label_position                | str         | C,C,c,0.00,0.00                                              | Node label position                        |
| node_label_rotation                | float       | 0.0                                                          | Node label rotation                        |
| node_label_transparency            | int         | 255                                                          | Node label transparency                    |
| node_label_width                   | float       | 200.0                                                        | Node label width                           |
| node_outline_color                 | str         | <span style="background: #CCCCCC;">\#CCCCCC</span>           | Node outline color                         |
| node_outline_color_key             | str         |                                                              | Node outline color mapping attribute key   |
| node_outline_color_mapper          | StyleMapper | StyleForegroundColorDefaultDiscreteMapper                    | Node outline color mapper                  |
| node_outline_width                 | float       | 2.0                                                          | Node outline width                         |
| node_padding                       | float       | 10.0                                                         | Node padding                               |
| node_selected                      | bool        | False                                                        | Whether node is selected                   |
| node_selected_color                | str         | <span style="background: #FFFF00;">\#FFFF00</span>           | Node selected color                        |
| node_selected_key                  | str         |                                                              | Node selected mapping attribute key        |
| node_selected_mapper               | StyleMapper | StylePassthroughMapper                                       | Node selected mapper                       |
| node_shape                         | str         | ELLIPSE                                                      | Node shape                                 |
| node_shape_key                     | str         |                                                              | Node shape mapping attribute key           |
| node_shape_mapper                  | StyleMapper | StyleNodeShapeDefaultDiscreteMapper                          | Node shape mapper                          |
| node_tooltip                       | str         |                                                              | Node tooltip                               |
| node_tooltip_key                   | str         |                                                              | Node tooltip mapping attribute key         |
| node_tooltip_mapper                | StyleMapper | StylePassthroughMapper                                       | Node tooltip mapper                        |
| node_transparency                  | int         | 255                                                          | Node transparency                          |
| node_visible                       | bool        |                                                              | Node visibility                            |
| node_visible_key                   | str         |                                                              | Node visibility mapping attribute key      |
| node_visible_mapper                | StyleMapper | StylePassthroughMapper                                       | Node visibility mapper                     |
| node_width                         | float       | 40.0                                                         | Node width                                 |
| node_width_key                     | str         |                                                              | Node width mapping attribute key           |
| node_width_mapper                  | StyleMapper | StyleNodeSizeDefaultContinuousMapper                         | Node Width Mapper                          |

!!! info "Info"

    `xxx_key` indicates the key in the node attributes. Please make sure that the corresponding value type is the same as the value type required by the `xxx` parameter.

### Edge

| Parameter                          | Type        | Default                                                      | Description                                        |
| ---------------------------------- | ----------- | ------------------------------------------------------------ | ---------------------------- |
| edge_curved                        | bool        | True                                                         | Whether edge is rendered as a curve                |
| edge_fill_color                    | str         | <span style="background: #999999;">\#999999</span>           | Edge color                                         |
| edge_fill_color_key                | str         |                                                              | Edge color mapping attribute key                   |
| edge_fill_color_mapper             | StyleMapper | StyleBackgroundColorDefaultDiscreteMapper                    | Edge color mapper                                  |
| edge_label                         | str         |                                                              | Edge label                                         |
| edge_label_key                     | str         |                                                              | Edge label mapping attribute key                   |
| edge_label_mapper                  | StyleMapper | StylePassthroughMapper                                       | Edge label mapper                                  |
| edge_label_autorotate              | bool        | False                                                        | Edge label autorotate                              |
| edge_label_background_color        | str         | <span style="background: #B6B6B6;">\#B6B6B6</span>           | Edge label background color                        |
| edge_label_background_shape        | str         | NONE                                                         | Edge label background shape                        |
| edge_label_background_transparency | int         | 255                                                          | Edge label background transparency                 |
| edge_label_color                   | str         | <span style="background: #000000; color: #FFFFFF;">\#000000</span> | Edge label color                                   |
| edge_label_font_face               | str         | Dialog,plain,10                                              | Edge label font                                    |
| edge_label_font_size               | int         | 10                                                           | Edge label font size                               |
| edge_label_position                | str         | C,C,c,0.00,0.00                                              | Edge label position                                |
| edge_label_rotation                | float       | 0.0                                                          | Edge label rotation angle                          |
| edge_label_transparency            | int         | 255                                                          | Edge label transparency                            |
| edge_label_width                   | float       | 200.0                                                        | Edge label width                                   |
| edge_line_type                     | str         | SOLID                                                        | Edge line shape                                    |
| edge_line_type_key                 | str         |                                                              | Edge line shape mapping attribute key              |
| edge_line_type_mapper              | StyleMapper | StyleLineTypeDefaultDiscreteMapper                           | Edge line shape mapper                             |
| edge_selected                      | bool        | False                                                        | Whether edge is selected                           |
| edge_selected_key                  | str         |                                                              | Edge selected mapping attribute key                |
| edge_selected_mapper               | StyleMapper | StylePassthroughMapper                                       | Edge selected mapper                               |
| edge_source_arrow_selected_color   | str         | <span style="background: #FFFF00;">\#FFFF00</span>           | Edge source node arrow selected color              |
| edge_source_arrow_shape            | str         | NONE                                                         | Edge source node arrow shape                       |
| edge_source_arrow_shape_key        | str         |                                                              | Edge source node arrow shape mapping attribute key |
| edge_source_arrow_shape_mapper     | StyleMapper | StyleArrowShapeDefaultDiscreteMapper                         | Edge source node arrow shape mapper                |
| edge_source_arrow_size             | float       | 6.0                                                          | Edge source node arrow size                        |
| edge_source_arrow_unselected_color | str         | #000000                                                      | Edge source node arrow unselected color            |
| edge_stroke_selected_color         | str         | <span style="background: #FF0000;">\#FF0000</span>           | Edge stroke selected color                         |
| edge_target_arrow_selected_color   | str         | <span style="background: #FFFF00;">\#FFFF00</span>           | Edge target node arrow selected color              |
| edge_target_arrow_shape            | str         | NONE                                                         | Edge target node arrow shape                       |
| edge_target_arrow_shape_key        | str         |                                                              | Edge target node arrow shape mapping property key  |
| edge_target_arrow_shape_mapper     | StyleMapper | StyleArrowShapeDefaultDiscreteMapper                         | Edge target node arrow shape mapper                |
| edge_target_arrow_size             | float       | 6.0                                                          | Edge target node arrow size                        |
| edge_target_arrow_unselected_color | str         | <span style="background: #000000; color: #FFFFFF;">\#000000</span> | Edge target node arrow unselected color            |
| edge_tooltip                       | str         |                                                              | Edge tooltip                                       |
| edge_tooltip_key                   | str         |                                                              | Edge tooltip mapping property key                  |
| edge_tooltip_mapper                | StyleMapper | StylePassthroughMapper                                       | Edge tooltip mapper                                |
| edge_transparency                  | int         | 170                                                          | Edge transparency                                  |
| edge_visible                       | bool        | True                                                         | Edge visibility                                    |
| edge_visible_key                   | str         |                                                              | Edge visibility map attribute key                  |
| edge_visible_mapper                | StyleMapper | StylePassthroughMapper                                       | Edge visibility mapper                             |
| edge_width                         | float       | 2.0                                                          | Edge width                                         |
| edge_z_order                       | float       | 0.0                                                          | Edge z-order                                       |

!!! info "Info"

    `xxx_key` indicates the key in the edge attributes. Please make sure that the corresponding value type is the same as the value type required by the `xxx` parameter.
