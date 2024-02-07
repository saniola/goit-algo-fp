from graph import Graph
from dijkstra import Dijkstra

# Creating a graph
graph = Graph()
graph.add_nodes(["A", "B", "C", "D", "E", "F", "G", "H"])
graph.add_weighted_edges(
    [
        ("A", "C", 1),
        ("A", "B", 2),
        ("C", "E", 2),
        ("B", "D", 3),
        ("D", "H", 2),
        ("C", "F", 2),
        ("E", "G", 2),
    ]
)

# Visualizing the graph
graph.visualize()

# Finding shortest paths using Dijkstra's algorithm
dijkstra = Dijkstra(graph)
shortest_paths = dijkstra.shortest_path("D")

print("Shortest paths from station 'D' to all other stations")
dijkstra.print_shortest_paths(shortest_paths["path"])

print("Lengths of the shortest paths from station 'D' to all other stations")
dijkstra.print_shortest_path_lengths(shortest_paths["dist"])
