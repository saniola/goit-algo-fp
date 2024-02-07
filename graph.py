import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        self.graph = nx.Graph(name="Graf")

    def add_nodes(self, nodes):
        self.graph.add_nodes_from(nodes)

    def add_weighted_edges(self, weighted_edges):
        self.graph.add_weighted_edges_from(weighted_edges)

    def visualize(self):
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_color="blue")
        labels = nx.get_edge_attributes(self.graph, "weight")
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)
        plt.show()
