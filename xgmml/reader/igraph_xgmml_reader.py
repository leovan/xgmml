import networkx as nx
import igraph as ig

from xgmml.reader.xgmml_reader import XGMMLReader


class IgraphXGMMLReader(XGMMLReader[ig.Graph]):
    def __init__(self, **kwargs):
        super(IgraphXGMMLReader, self).__init__(**kwargs)

    def _networkx_to(self, graph: nx.MultiGraph, **kwargs) -> ig.Graph:
        return ig.Graph.from_networkx(graph)


__all__ = ['IgraphXGMMLReader']
