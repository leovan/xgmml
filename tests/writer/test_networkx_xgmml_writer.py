import unittest
import matplotlib as mpl

from xgmml.reader.networkx_xgmml_reader import NetworkxXGMMLReader
from xgmml.writer.networkx_xgmml_writer import NetworkxXGMMLWriter
from xgmml.style.style_mapper import *
from xgmml.utils.path_utils import *


class StyleNodeSizeMapper(StyleNodeSizeDefaultContinuousMapper):
    def __init__(self, values, **kwargs):
        super(StyleNodeSizeMapper, self).__init__(values, **kwargs)

        self._min_size = 40
        self._max_size = 150


class StyleNodeLabelFontSizeMapper(StyleFontSizeDefaultContinuousMapper):
    def __init__(self, values, **kwargs):
        super(StyleNodeLabelFontSizeMapper, self).__init__(values, **kwargs)

        self._min_size = 10
        self._max_size = 40


class StyleNodeFillColorMapper(StyleColorContinuousMapper):
    def __init__(self, values, **kwargs):
        colors = ['#0066CC', '#FFFFFF', '#FFFF00']
        colormap = mpl.colors.LinearSegmentedColormap.from_list('custom', colors)

        super(StyleNodeFillColorMapper, self).__init__(
            values, colormap=colormap, **kwargs
        )


class NetworkxXGMMLWriterTestCase(unittest.TestCase):
    def setUp(self):
        xgmml_reader = NetworkxXGMMLReader()
        self._yeast_perturbation_graph = xgmml_reader.read(
            DATA_DIR / 'tests' / 'yeast_perturbation.xgmml'
        )

        self._xgmml_writer = NetworkxXGMMLWriter()

    def test_write_default(self):
        self._xgmml_writer.write(
            self._yeast_perturbation_graph,
            DATA_DIR / 'tests' / 'yeast_perturbation_networkx_default.xgmml',
            graph_label='Yeast Perturbation (Default)',
        )

    def test_write_restore_style(self):
        self._xgmml_writer.write(
            self._yeast_perturbation_graph,
            DATA_DIR / 'tests' / 'yeast_perturbation_networkx_restore.xgmml',
            graph_label='Yeast Perturbation (Restore Style)',
            node_label_key='COMMON',
            node_width_key='degree.layout',
            node_width_mapper=StyleNodeSizeMapper,
            node_height_key='degree.layout',
            node_height_mapper=StyleNodeSizeMapper,
            node_label_font_size_key='Degree',
            node_label_font_size_mapper=StyleNodeLabelFontSizeMapper,
            node_fill_color_key='gal1RGexp',
            node_fill_color_mapper=StyleNodeFillColorMapper,
        )

    def test_write_custom_style(self):
        self._xgmml_writer.write(
            self._yeast_perturbation_graph,
            DATA_DIR / 'tests' / 'yeast_perturbation_networkx_custom.xgmml',
            graph_label='Yeast Perturbation (Custom Style)',
            node_label_key='COMMON',
            node_width_key='degree.layout',
            node_width_mapper=StyleNodeSizeMapper,
            node_height_key='degree.layout',
            node_height_mapper=StyleNodeSizeMapper,
            node_label_font_size_key='Degree',
            node_label_font_size_mapper=StyleNodeLabelFontSizeMapper,
            node_fill_color_key='gal1RGexp',
            node_fill_color_mapper=StyleColorDefaultContinuousMapper,
        )


if __name__ == '__main__':
    unittest.main()
