import networkx as nx
import igraph as ig

from xgmml.writer.xgmml_writer import XGMMLWriter


class IgraphXGMMLWriter(XGMMLWriter[ig.Graph]):
    def __init__(self, **kwargs):
        super(IgraphXGMMLWriter, self).__init__(**kwargs)

    def _to_networkx(self, graph: ig.Graph, **kwargs) -> nx.MultiGraph:
        return ig.Graph.to_networkx(graph)


__all__ = ['IgraphXGMMLWriter']
