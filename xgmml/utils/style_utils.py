import matplotlib as mpl


NODE_SHAPES = [
    'ELLIPSE',
    'RECTANGLE',
    'HEXAGON',
    'OCTAGON',
    'DIAMOND',
    'TRIANGLE',
    'ROUNDED_RECTANGLE',
]


LINE_TYPES = [
    'SOLID',
    'LONG_DASH',
    'DOT',
    'DASH_DOT',
    'EQUAL_DASH',
    'PARALLEL_LINES',
    'VERTICAL_SLASH',
    'FORWARD_SLASH',
    'BACKWARD_SLASH',
    'CONTIGUOUS_ARROW',
    'SEPARATE_ARROW',
    'SINEWAVE',
    'ZIGZAG',
]


ARROW_SHAPES = [
    'ARROW',
    'ARROW_SHORT',
    'CIRCLE',
    'CROSS_DELTA',
    'CROSS_OPEN_DELTA',
    'DELTA',
    'DELTA_SHORT_1',
    'DELTA_SHORT_2',
    'DIAMOND',
    'DIAMOND_SHORT_1',
    'DIAMOND_SHORT_2',
    'HALF_BOTTOM',
    'HALF_CIRCLE',
    'HALF_TOP',
    'NONE',
    'OPEN_CIRCLE',
    'OPEN_DELTA',
    'OPEN_DIAMOND',
    'OPEN_HALF_CIRCLE',
    'OPEN_SQUARE',
    'SQUARE',
    'T',
]


DEFAULT_FOREGROUND_COLOR_PALETTE = [
    '#1783FF',
    '#00C9C9',
    '#F0884D',
    '#D580FF',
    '#7863FF',
    '#60C42D',
    '#BD8F24',
    '#FF80CA',
    '#2491B3',
    '#17C76F',
]


def add_alpha(color_hex, alpha):
    r, g, b = mpl.colors.to_rgb(color_hex)

    return mpl.colors.to_hex(
        (
            r * alpha + 1 * (1 - alpha),
            g * alpha + 1 * (1 - alpha),
            b * alpha + 1 * (1 - alpha),
        )
    )


DEFAULT_BACKGROUND_COLOR_PALETTE = [
    add_alpha(color_hex, 0.2) for color_hex in DEFAULT_FOREGROUND_COLOR_PALETTE
]


__all__ = [
    'NODE_SHAPES',
    'LINE_TYPES',
    'ARROW_SHAPES',
    'DEFAULT_FOREGROUND_COLOR_PALETTE',
    'DEFAULT_BACKGROUND_COLOR_PALETTE',
    'add_alpha',
]
