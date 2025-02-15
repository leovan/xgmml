import networkx as nx

from xgmml.writer.xgmml_writer import XGMMLWriter


class NetworkxXGMMLWriter(XGMMLWriter[nx.MultiGraph]):
    def __init__(self, **kwargs):
        super(NetworkxXGMMLWriter, self).__init__(**kwargs)

    def _to_networkx(self, graph: nx.MultiGraph, **kwargs) -> nx.MultiGraph:
        return graph


__all__ = ['NetworkxXGMMLWriter']
