import unittest

from xgmml.reader.igraph_xgmml_reader import IgraphXGMMLReader
from xgmml.writer.igraph_xgmml_writer import IgraphXGMMLWriter
from xgmml.utils.path_utils import *


class IgraphXGMMLTestCase(unittest.TestCase):
    def setUp(self):
        xgmml_reader = IgraphXGMMLReader()
        self._yeast_perturbation_graph = xgmml_reader.read(
            DATA_DIR / 'tests' / 'yeast_perturbation.xgmml'
        )

        self._xgmml_writer = IgraphXGMMLWriter()

    def test_write_default(self):
        self._xgmml_writer.write(
            self._yeast_perturbation_graph,
            DATA_DIR / 'tests' / 'yeast_perturbation_igraph_default.xgmml',
            graph_label='Yeast Perturbation (Default)',
        )


if __name__ == '__main__':
    unittest.main()
