---
icon: lucide/variable
---

# 参数

!!! tip "提示"

    样式相关参数细节请参见：<https://cytoscape.leovan.tech/styles/>。

## 读取器

| 参数       | 类型 | 默认值 | 说明       |
| ---------- | ---- | ------ | ---------- |
| xgmml_path | str  |        | XGMML 路径 |

## 写入器

### 图

| 参数                       | 类型   | 默认值                                             | 说明               |
| -------------------------- | ------ | -------------------------------------------------- | ------------------ |
| graph_annotation_selection | bool   | False                                              | 图注释可否选中     |
| graph_background_color     | str    | <span style="background: #FFFFFF;">\#FFFFFF</span> | 图背景颜色         |
| graph_center_x_location    | float  | 自动生成                                           | 图中心 X 轴位置    |
| graph_center_y_location    | float  | 自动生成                                           | 图中心 Y 轴位置    |
| graph_center_z_location    | float  | 0                                                  | 图中心 Z 轴位置    |
| graph_cy_document_version  | str    | 3.0                                                | Cytoscape 文档版本 |
| graph_depth                | float  | 0                                                  | 图深度             |
| graph_description          | str    | N/A                                                | 图描述             |
| graph_edge_selection       | bool   | False                                              | 图边可否选中       |
| graph_force_high_detail    | bool   | False                                              | 图是否强制显示细节 |
| graph_format               | str    | Cytoscape-XGMML                                    | 图格式             |
| graph_height               | float  | 自动生成                                           | 图高度             |
| graph_id                   | str    | 自动生成                                           | 图 ID              |
| graph_identifier           | str    | N/A                                                | 图标识             |
| graph_label                | str    | 自动生成                                           | 图名称             |
| graph_layout               | Layout | KamadaKawaiLayout                                  | 图布局算法         |
| graph_layout_kwargs        | dict   | {}                                                 | 图布局算法参数     |
| graph_node_label_selection | bool   | False                                              | 图点标签可否选中   |
| graph_node_selection       | bool   | True                                               | 图点可否选中       |
| graph_scale_factor         | float  | 1                                                  | 图缩放因子         |
| graph_source               | str    | https://xgmml.leovan.tech                          | 图来源             |
| graph_type                 | str    | N/A                                                | 图类型             |
| graph_width                | float  | 自动生成                                           | 图宽度             |

### 点

| 参数                               | 类型        | 默认值                                                       | 说明                   |
| ---------------------------------- | ----------- | ------------------------------------------------------------ | ---------------------- |
| node_border_stroke                 | str         | SOLID                                                        | 点描边线型             |
| node_border_transparency           | int         | 255                                                          | 点描边透明度           |
| node_depth                         | float       | 0.0                                                          | 点深度                 |
| node_fill_color                    | str         | <span style="background: #FFFFFF;">\#FFFFFF</span>           | 点填充颜色             |
| node_fill_color_key                | str         |                                                              | 点填充颜色映射属性键   |
| node_fill_color_mapper             | StyleMapper | StyleBackgroundColorDefaultDiscreteMapper                    | 点填充颜色映射器       |
| node_height                        | float       | 40.0                                                         | 点高度                 |
| node_height_key                    | str         |                                                              | 点高度映射属性键       |
| node_height_mapper                 | StyleMapper | StyleNodeSizeDefaultContinuousMapper                         | 点高度映射器           |
| node_label                         | str         |                                                              | 点标签                 |
| node_label_key                     | str         |                                                              | 点标签映射属性键       |
| node_label_mapper                  | str         | StylePassthroughMapper                                       | 点标签映射器           |
| node_label_background_color        | str         | <span style="background: #B6B6B6;">\#B6B6B6</span>           | 点标签背景色           |
| node_label_background_shape        | str         | NONE                                                         | 点标签背景形状         |
| node_label_background_transparency | int         | 255                                                          | 点标签背景透明度       |
| node_label_color                   | str         | <span style="background: #333333; color: #FFFFFF;">\#333333</span> | 点标签颜色             |
| node_label_font_face               | str         | Dialog,plain,12                                              | 点标签字体             |
| node_label_font_size               | int         | 10                                                           | 点标签字号             |
| node_label_font_size_key           | str         |                                                              | 点标签字号映射属性键   |
| node_label_font_size_mapper        | StyleMapper | StyleFontSizeDefaultContinuousMapper                         | 点标签字号映射器       |
| node_label_position                | str         | C,C,c,0.00,0.00                                              | 点标签位置             |
| node_label_rotation                | float       | 0.0                                                          | 点标签旋转角度         |
| node_label_transparency            | int         | 255                                                          | 点标签透明度           |
| node_label_width                   | float       | 200.0                                                        | 点标签宽度             |
| node_outline_color                 | str         | <span style="background: #CCCCCC;">\#CCCCCC</span>           | 点描边颜色             |
| node_outline_color_key             | str         |                                                              | 点描边颜色映射属性键   |
| node_outline_color_mapper          | StyleMapper | StyleForegroundColorDefaultDiscreteMapper                    | 点描边颜色映射器       |
| node_outline_width                 | float       | 2.0                                                          | 点描边宽度             |
| node_padding                       | float       | 10.0                                                         | 点内边距               |
| node_selected                      | bool        | False                                                        | 点是否被选中           |
| node_selected_color                | str         | <span style="background: #FFFF00;">\#FFFF00</span>           | 点被选中后颜色         |
| node_selected_key                  | str         |                                                              | 点是否被选中映射属性键 |
| node_selected_mapper               | StyleMapper | StylePassthroughMapper                                       | 点是否被选中器映射器   |
| node_shape                         | str         | ELLIPSE                                                      | 点形状                 |
| node_shape_key                     | str         |                                                              | 点形状映射属性键       |
| node_shape_mapper                  | StyleMapper | StyleNodeShapeDefaultDiscreteMapper                          | 点形状映射器           |
| node_tooltip                       | str         |                                                              | 点提示                 |
| node_tooltip_key                   | str         |                                                              | 点提示映射属性键       |
| node_tooltip_mapper                | StyleMapper | StylePassthroughMapper                                       | 点提示映射器           |
| node_transparency                  | int         | 255                                                          | 点透明度               |
| node_visible                       | bool        |                                                              | 点可见性               |
| node_visible_key                   | str         |                                                              | 点可见性映射属性键     |
| node_visible_mapper                | StyleMapper | StylePassthroughMapper                                       | 点可见性映射属器       |
| node_width                         | float       | 40.0                                                         | 点宽度                 |
| node_width_key                     | str         |                                                              | 点宽度映射属性键       |
| node_width_mapper                  | StyleMapper | StyleNodeSizeDefaultContinuousMapper                         | 点宽度映射器           |

!!! info "信息"

    `xxx_key` 表示点属性中的键，请确保对应的值类型与 `xxx` 参数要求的值类型相同。

### 边

| 参数                               | 类型        | 默认值                                                       | 说明                         |
| ---------------------------------- | ----------- | ------------------------------------------------------------ | ---------------------------- |
| edge_curved                        | bool        | True                                                         | 边是否渲染为曲线             |
| edge_fill_color                    | str         | <span style="background: #999999;">\#999999</span>           | 边颜色                       |
| edge_fill_color_key                | str         |                                                              | 边颜色映射属性键             |
| edge_fill_color_mapper             | StyleMapper | StyleBackgroundColorDefaultDiscreteMapper                    | 边颜色映射器                 |
| edge_label                         | str         |                                                              | 边标签                       |
| edge_label_key                     | str         |                                                              | 边标签映射属性键             |
| edge_label_mapper                  | StyleMapper | StylePassthroughMapper                                       | 边标签映射器                 |
| edge_label_autorotate              | bool        | False                                                        | 边标签自动旋转               |
| edge_label_background_color        | str         | <span style="background: #B6B6B6;">\#B6B6B6</span>           | 边标签背景颜色               |
| edge_label_background_shape        | str         | NONE                                                         | 边标签背景形状               |
| edge_label_background_transparency | int         | 255                                                          | 边标签背景透明度             |
| edge_label_color                   | str         | <span style="background: #000000; color: #FFFFFF;">\#000000</span> | 边标签颜色                   |
| edge_label_font_face               | str         | Dialog,plain,10                                              | 边标签字体                   |
| edge_label_font_size               | int         | 10                                                           | 边标签字号                   |
| edge_label_position                | str         | C,C,c,0.00,0.00                                              | 边标签位置                   |
| edge_label_rotation                | float       | 0.0                                                          | 边标签旋转角度               |
| edge_label_transparency            | int         | 255                                                          | 边标签透明度                 |
| edge_label_width                   | float       | 200.0                                                        | 边标签宽度                   |
| edge_line_type                     | str         | SOLID                                                        | 边线形                       |
| edge_line_type_key                 | str         |                                                              | 边线形映射属性键             |
| edge_line_type_mapper              | StyleMapper | StyleLineTypeDefaultDiscreteMapper                           | 边线形映射器                 |
| edge_selected                      | bool        | False                                                        | 边是否被选中                 |
| edge_selected_key                  | str         |                                                              | 边是否被选中映射属性键       |
| edge_selected_mapper               | StyleMapper | StylePassthroughMapper                                       | 边是否被选中映射器           |
| edge_source_arrow_selected_color   | str         | <span style="background: #FFFF00;">\#FFFF00</span>           | 边源节点箭头选中颜色         |
| edge_source_arrow_shape            | str         | NONE                                                         | 边源节点箭头形状             |
| edge_source_arrow_shape_key        | str         |                                                              | 边源节点箭头形状映射属性键   |
| edge_source_arrow_shape_mapper     | StyleMapper | StyleArrowShapeDefaultDiscreteMapper                         | 边源节点箭头形状映射器       |
| edge_source_arrow_size             | float       | 6.0                                                          | 边源节点箭头大小             |
| edge_source_arrow_unselected_color | str         | #000000                                                      | 边源节点箭头未选中颜色       |
| edge_stroke_selected_color         | str         | <span style="background: #FF0000;">\#FF0000</span>           | 边描边选中颜色               |
| edge_target_arrow_selected_color   | str         | <span style="background: #FFFF00;">\#FFFF00</span>           | 边目标节点箭头选中颜色       |
| edge_target_arrow_shape            | str         | NONE                                                         | 边目标节点箭头形状           |
| edge_target_arrow_shape_key        | str         |                                                              | 边目标节点箭头形状映射属性键 |
| edge_target_arrow_shape_mapper     | StyleMapper | StyleArrowShapeDefaultDiscreteMapper                         | 边目标节点箭头形状映射器     |
| edge_target_arrow_size             | float       | 6.0                                                          | 边目标节点箭头大小           |
| edge_target_arrow_unselected_color | str         | <span style="background: #000000; color: #FFFFFF;">\#000000</span> | 边目标节点箭头未选中颜色     |
| edge_tooltip                       | str         |                                                              | 边提示                       |
| edge_tooltip_key                   | str         |                                                              | 边提示映射属性键             |
| edge_tooltip_mapper                | StyleMapper | StylePassthroughMapper                                       | 边提示映射器                 |
| edge_transparency                  | int         | 170                                                          | 边透明度                     |
| edge_visible                       | bool        | True                                                         | 边可见性                     |
| edge_visible_key                   | str         |                                                              | 边可见性映射属性键           |
| edge_visible_mapper                | StyleMapper | StylePassthroughMapper                                       | 边可见性映射器               |
| edge_width                         | float       | 2.0                                                          | 边宽度                       |
| edge_z_order                       | float       | 0.0                                                          | 边 Z 轴顺序                  |

!!! info "信息"

    `xxx_key` 表示边属性中的键，请确保对应的值类型与 `xxx` 参数要求的值类型相同。
