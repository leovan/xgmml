import sys
import networkx as nx

from abc import ABC, abstractmethod
from math import dist


class Layout(ABC):
    def __init__(
        self, name, canvas_width=1200, canvas_height=900, subgraph_spacing=100, **kwargs
    ):
        self._name = name
        self._canvas_width = canvas_width
        self._canvas_height = canvas_height
        self._subgraph_spacing = subgraph_spacing

    @property
    def name(self):
        return self._name

    def _calc_auto_scale(
        self,
        graph: nx.Graph,
        graph_layout: dict[str, tuple[float, float]],
        nodes_size: dict[str, tuple[float, float]],
        min_node_spacing_ratio=2.0,
    ) -> float:
        edge_node_distances = []
        for node_source, node_target in graph.edges():
            edge_node_distances.append(
                dist(graph_layout[node_source], graph_layout[node_target])
            )

        node_distances = []
        nodes = list(graph.nodes())
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                node_distances.append(
                    dist(graph_layout[nodes[i]], graph_layout[nodes[j]])
                )

        min_node_distance = max(min(edge_node_distances), 0.1)
        max_node_distance = max(node_distances)
        avg_node_size = sum([(w + h) / 2.0 for w, h in nodes_size.values()]) / len(
            nodes_size
        )

        return (
            min_node_spacing_ratio
            * avg_node_size
            * max_node_distance
            / min_node_distance
            / 2
        )

    def _get_graph_layout_stats(self, subgraph_layout: dict[str, tuple[float, float]]):
        node_x_list = [node_x for node_x, _ in subgraph_layout.values()]
        node_y_list = [node_y for _, node_y in subgraph_layout.values()]

        return {
            'min_x': min(node_x_list),
            'max_x': max(node_x_list),
            'min_y': min(node_y_list),
            'max_y': max(node_y_list),
            'width': max(node_x_list) - min(node_x_list),
            'height': max(node_y_list) - min(node_y_list),
        }

    def _calc_max_width(
        self, subgraphs_layout: list[dict[str, tuple[float, float]]], max_iterations=10
    ) -> float:
        subgraphs_layout_stats = [
            self._get_graph_layout_stats(subgraph_layout)
            for subgraph_layout in subgraphs_layout
        ]

        min_x = sys.float_info.max
        max_x = sys.float_info.min

        for subgraph_layout_stats in subgraphs_layout_stats:
            min_x = min(min_x, subgraph_layout_stats['min_x'])
            max_x = max(max_x, subgraph_layout_stats['max_x'])

        width = max_x - min_x
        max_width = max(width, self._canvas_width)
        canvas_ratio = self._canvas_width / self._canvas_height

        for _ in range(max_iterations):
            next_x_start = 0.0
            next_y_start = 0.0
            y_max = 0.0

            for subgraph_layout_stat in subgraphs_layout_stats:
                next_x_start += subgraph_layout_stat['width'] + self._subgraph_spacing
                y_max = max(y_max, subgraph_layout_stat['height'])

                if next_x_start > max_width:
                    next_x_start = 0.0
                    next_y_start += y_max + self._subgraph_spacing
                    y_max = 0.0

            layout_ratio = max_width / (next_y_start + y_max)
            max_width *= canvas_ratio / layout_ratio

        return max_width

    def _offset_subgraph_layout(
        self,
        subgraph_layout: dict[str, tuple[float, float]],
        subgraph_layout_stats: dict,
        offset_x,
        offset_y,
    ):
        min_x = subgraph_layout_stats['min_x']
        min_y = subgraph_layout_stats['min_y']

        for node_id, (node_x, node_y) in subgraph_layout.items():
            subgraph_layout[node_id] = (
                node_x + offset_x - min_x,
                node_y + offset_y - min_y,
            )

    def layout(
        self,
        graph: nx.MultiGraph,
        nodes_size: dict[str, tuple[float, float]] = None,
        **kwargs,
    ) -> dict[str, tuple[float, float]]:
        undirected_graph = graph.to_undirected()
        connected_components = list(nx.connected_components(undirected_graph))
        connected_components = sorted(
            connected_components, key=lambda x: len(x), reverse=True
        )
        subgraphs = [graph.subgraph(nodes).copy() for nodes in connected_components]

        subgraphs_layout = [
            self._subgraph_layout(subgraph, nodes_size) for subgraph in subgraphs
        ]

        max_width = self._calc_max_width(subgraphs_layout, **kwargs)
        next_x_start = 0.0
        next_y_start = 0.0
        y_max = 0.0

        for subgraph_layout in subgraphs_layout:
            subgraph_layout_stats = self._get_graph_layout_stats(subgraph_layout)
            self._offset_subgraph_layout(
                subgraph_layout, subgraph_layout_stats, next_x_start, next_y_start
            )

            next_x_start += subgraph_layout_stats['width'] + self._subgraph_spacing
            y_max = max(y_max, subgraph_layout_stats['height'])

            if next_x_start > max_width:
                next_x_start = 0.0
                next_y_start += y_max + self._subgraph_spacing
                y_max = 0.0

        layout = {}
        for subgraph_layout in subgraphs_layout:
            for node_id, node_position in subgraph_layout.items():
                layout[node_id] = node_position

        return layout

    @abstractmethod
    def _subgraph_layout(
        self,
        subgraph: nx.Graph,
        nodes_size: dict[str, tuple[float, float]] = None,
    ) -> dict[str, tuple[float, float]]:
        raise NotImplementedError()


__all__ = ['Layout']
