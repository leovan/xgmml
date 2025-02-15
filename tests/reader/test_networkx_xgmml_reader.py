import unittest

from xgmml.reader.networkx_xgmml_reader import NetworkxXGMMLReader
from xgmml.utils.path_utils import *


class NetworkxXGMMLReaderTestCase(unittest.TestCase):
    def test_read(self):
        xgmml_reader = NetworkxXGMMLReader()
        yeast_perturbation_graph = xgmml_reader.read(
            DATA_DIR / 'tests' / 'yeast_perturbation.xgmml'
        )

        self.assertTrue(yeast_perturbation_graph.is_directed())

        self.assertEqual(330, len(yeast_perturbation_graph.nodes))
        self.assertEqual(359, len(yeast_perturbation_graph.edges))

        node = yeast_perturbation_graph.nodes['813']

        self.assertEqual('YKR026C', node['label'])
        self.assertEqual(False, node['IsSingleNode'])
        self.assertEqual(1, node['Degree'])
        self.assertEqual(0.0, node['BetweennessCentrality'])

        edge = yeast_perturbation_graph.edges['813', '811', 0]

        self.assertEqual(False, edge['isInPath'])
        self.assertEqual(496.0, edge['EdgeBetweenness'])


if __name__ == '__main__':
    unittest.main()
