import igraph as ig
import networkx as nx

from xgmml.layout.base_layout import Layout


class KamadaKawaiLayout(Layout):
    def __init__(self, **kwargs):
        super(KamadaKawaiLayout, self).__init__('Kamada-Kawai Layout', **kwargs)

    def _subgraph_layout(
        self, subgraph: nx.Graph, nodes_size: dict[str, tuple[float, float]] = None
    ) -> dict[str, tuple[float, float]]:
        ig_subgraph: ig.Graph = ig.Graph.from_networkx(subgraph)
        ig_subgraph_layout: ig.Layout = ig_subgraph.layout_kamada_kawai()

        subgraph_layout = {}
        for node_id, node_position in zip(subgraph.nodes, ig_subgraph_layout.coords):
            subgraph_layout[node_id] = node_position

        scale = self._calc_auto_scale(subgraph, subgraph_layout, nodes_size)

        return nx.rescale_layout_dict(subgraph_layout, scale=scale)


__all__ = ['KamadaKawaiLayout']
