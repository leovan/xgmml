import unittest
import matplotlib as mpl

from xgmml.style.style_mapper import *
from xgmml.utils.style_utils import *


class StyleMapperTestCase(unittest.TestCase):
    def test_style_discrete_mapper(self):
        values = [f'{i:0>2}' for i in range(10)]

        mapper = StyleDiscreteMapper(values, NODE_SHAPES)

        self.assertEqual(NODE_SHAPES[0], mapper.map('00'))
        self.assertEqual(NODE_SHAPES[0], mapper.map('07'))

    def test_style_continuous_mapper(self):
        values = [i for i in range(10)]

        mapper = StyleContinuousMapper(values)

        self.assertEqual(0, mapper.map(0))
        self.assertEqual(0.5, mapper.map(4.5))
        self.assertEqual(1, mapper.map(9))

    def test_style_discrete_color_mapper(self):
        colormap = mpl.colormaps['tab10']
        colors = colormap.colors
        values = [f'{i:0>2}' for i in range(20)]

        mapper = StyleColorDiscreteMapper(values, colormap)

        self.assertEqual(mpl.colors.to_hex(colors[0]), mapper.map('00'))
        self.assertEqual(mpl.colors.to_hex(colors[0]), mapper.map('10'))
        self.assertEqual(mpl.colors.to_hex(colors[2]), mapper.map('02'))
        self.assertEqual(mpl.colors.to_hex(colors[2]), mapper.map('12'))

    def test_style_continuous_color_mapper(self):
        colormap = mpl.colormaps['viridis']
        values = [i for i in range(20)]

        mapper = StyleColorContinuousMapper(values, colormap)

        self.assertEqual(mpl.colors.to_hex(colormap(0.0)).upper(), mapper.map(0))
        self.assertEqual(mpl.colors.to_hex(colormap(1.0)).upper(), mapper.map(19))


if __name__ == '__main__':
    unittest.main()
