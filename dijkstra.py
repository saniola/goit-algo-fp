import heapq


class Dijkstra:
    def __init__(self, graph):
        self.graph = graph

    def shortest_path(self, start):
        dist = {node: float("infinity") for node in self.graph.graph}
        paths = {node: [] for node in self.graph.graph}
        dist[start] = 0
        priority_queue = [(0, start, [start])]

        while priority_queue:
            cur_dist, cur_node, cur_path = heapq.heappop(priority_queue)

            if cur_dist > dist[cur_node]:
                continue

            for neighbor, weight in self.graph.graph[cur_node].items():
                distance = cur_dist + weight["weight"]

                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    new_path = cur_path + [neighbor]
                    paths[neighbor] = new_path
                    heapq.heappush(priority_queue, (distance, neighbor, new_path))

        return {"path": paths, "dist": dist}

    def print_shortest_paths(self, shortest_paths):
        for obj in shortest_paths:
            print(obj, "=>", shortest_paths[obj])

    def print_shortest_path_lengths(self, shortest_path_lengths):
        for obj in shortest_path_lengths:
            print(obj, "=>", shortest_path_lengths[obj])
