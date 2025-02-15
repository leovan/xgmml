import unittest

from xgmml.reader.igraph_xgmml_reader import IgraphXGMMLReader
from xgmml.utils.path_utils import *


class IgraphXGMMLReaderTest(unittest.TestCase):
    def test_read(self):
        xgmml_reader = IgraphXGMMLReader()
        yeast_perturbation_graph = xgmml_reader.read(
            DATA_DIR / 'tests' / 'yeast_perturbation.xgmml'
        )

        self.assertTrue(yeast_perturbation_graph.is_directed())

        self.assertEqual(330, yeast_perturbation_graph.vcount())
        self.assertEqual(359, yeast_perturbation_graph.ecount())

        node = yeast_perturbation_graph.vs.find(id='813')

        self.assertEqual('YKR026C', node['label'])
        self.assertEqual(False, node['IsSingleNode'])
        self.assertEqual(1, node['Degree'])
        self.assertEqual(0.0, node['BetweennessCentrality'])

        edge = yeast_perturbation_graph.es[0]

        self.assertEqual(False, edge['isInPath'])
        self.assertEqual(496.0, edge['EdgeBetweenness'])


if __name__ == '__main__':
    unittest.main()
