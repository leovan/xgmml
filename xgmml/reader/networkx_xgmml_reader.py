import networkx as nx

from xgmml.reader.xgmml_reader import XGMMLReader


class NetworkxXGMMLReader(XGMMLReader[nx.MultiGraph]):
    def __init__(self, **kwargs):
        super(NetworkxXGMMLReader, self).__init__(**kwargs)

    def _networkx_to(self, graph: nx.MultiGraph, **kwargs) -> nx.MultiGraph:
        return graph


__all__ = ['NetworkxXGMMLReader']
