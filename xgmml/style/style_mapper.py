import matplotlib as mpl

from abc import ABC, abstractmethod

from xgmml.utils.style_utils import *


class StyleMapper(ABC):
    def __init__(self, values: list, **kwargs):
        self._values = values

    @abstractmethod
    def map(self, value):
        raise NotImplementedError()


class StylePassthroughMapper(StyleMapper):
    def __init__(self, values: list, **kwargs):
        super(StylePassthroughMapper, self).__init__(values)

    def map(self, value):
        return value


class StyleDiscreteMapper(StyleMapper):
    def __init__(self, values: list, styles: list, **kwargs):
        super(StyleDiscreteMapper, self).__init__(values)

        self._styles = styles
        self._categories = sorted(set(values), key=self._sort_key)

    def _sort_key(self, value):
        return value

    def map(self, value):
        category_idx = self._categories.index(value)
        style_idx = category_idx % len(self._styles)

        return self._styles[style_idx]


class StyleContinuousMapper(StyleMapper):
    def __init__(self, values: list, **kwargs):
        super(StyleContinuousMapper, self).__init__(values)

        self._min_value = min(self._values)
        self._max_value = max(self._values)

    def _transform_value(self, value) -> float:
        if self._max_value - self._min_value == 0:
            return 0.0

        return (value - self._min_value) / (self._max_value - self._min_value)

    def map(self, value):
        return self._transform_value(value)


class StyleColorDiscreteMapper(StyleMapper):
    def __init__(self, values: list, colormap: mpl.colors.ListedColormap, **kwargs):
        super(StyleColorDiscreteMapper, self).__init__(values)

        self._colors = colormap.colors
        self._categories = sorted(set(values), key=self._sort_key)

    def _sort_key(self, value):
        return value

    def map(self, value):
        category_idx = self._categories.index(value)
        color_idx = category_idx % len(self._colors)

        return mpl.colors.to_hex(self._colors[color_idx])


class StyleColorContinuousMapper(StyleMapper):
    def __init__(
        self, values: list, colormap: mpl.colors.LinearSegmentedColormap, **kwargs
    ):
        super(StyleColorContinuousMapper, self).__init__(values)

        self._colormap = colormap
        self._normalizer = mpl.colors.Normalize(vmin=min(values), vmax=max(values))

    def map(self, value):
        color = self._colormap(self._normalizer(value))

        return mpl.colors.to_hex(color).upper()


class StyleNodeShapeDefaultDiscreteMapper(StyleDiscreteMapper):
    def __init__(self, values, **kwargs):
        super(StyleNodeShapeDefaultDiscreteMapper, self).__init__(
            values, NODE_SHAPES, **kwargs
        )


class StyleNodeSizeDefaultContinuousMapper(StyleContinuousMapper):
    def __init__(self, values, **kwargs):
        super(StyleNodeSizeDefaultContinuousMapper, self).__init__(values, **kwargs)

        self._min_size = 10
        self._max_size = 40

    def _transform_value(self, value):
        transformed_value = super(
            StyleNodeSizeDefaultContinuousMapper, self
        )._transform_value(value)

        return int(
            transformed_value * (self._max_size - self._min_size) + self._min_size
        )


class StyleForegroundColorDefaultDiscreteMapper(StyleColorDiscreteMapper):
    def __init__(self, values, **kwargs):
        super(StyleForegroundColorDefaultDiscreteMapper, self).__init__(
            values,
            mpl.colors.ListedColormap(DEFAULT_FOREGROUND_COLOR_PALETTE),
            **kwargs,
        )


class StyleBackgroundColorDefaultDiscreteMapper(StyleColorDiscreteMapper):
    def __init__(self, values, **kwargs):
        super(StyleBackgroundColorDefaultDiscreteMapper, self).__init__(
            values,
            mpl.colors.ListedColormap(DEFAULT_BACKGROUND_COLOR_PALETTE),
            **kwargs,
        )


class StyleColorDefaultContinuousMapper(StyleColorContinuousMapper):
    def __init__(self, values, **kwargs):
        super(StyleColorDefaultContinuousMapper, self).__init__(
            values, mpl.colormaps['coolwarm'], **kwargs
        )


class StyleFontSizeDefaultContinuousMapper(StyleContinuousMapper):
    def __init__(self, values, **kwargs):
        super(StyleFontSizeDefaultContinuousMapper, self).__init__(values, **kwargs)

        self._min_size = 10
        self._max_size = 40

    def _transform_value(self, value):
        transformed_value = super(
            StyleFontSizeDefaultContinuousMapper, self
        )._transform_value(value)

        return int(
            transformed_value * (self._max_size - self._min_size) + self._min_size
        )


class StyleLineTypeDefaultDiscreteMapper(StyleDiscreteMapper):
    def __init__(self, values, **kwargs):
        super(StyleLineTypeDefaultDiscreteMapper, self).__init__(
            values, LINE_TYPES, **kwargs
        )


class StyleArrowShapeDefaultDiscreteMapper(StyleDiscreteMapper):
    def __init__(self, values, **kwargs):
        super(StyleArrowShapeDefaultDiscreteMapper, self).__init__(
            values, ARROW_SHAPES, **kwargs
        )


__all__ = [
    'StyleMapper',
    'StylePassthroughMapper',
    'StyleDiscreteMapper',
    'StyleContinuousMapper',
    'StyleColorDiscreteMapper',
    'StyleColorContinuousMapper',
    'StyleNodeShapeDefaultDiscreteMapper',
    'StyleNodeSizeDefaultContinuousMapper',
    'StyleForegroundColorDefaultDiscreteMapper',
    'StyleBackgroundColorDefaultDiscreteMapper',
    'StyleColorDefaultContinuousMapper',
    'StyleFontSizeDefaultContinuousMapper',
    'StyleLineTypeDefaultDiscreteMapper',
    'StyleArrowShapeDefaultDiscreteMapper',
]
