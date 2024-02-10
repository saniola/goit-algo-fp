import heapq
import networkx as nx
import matplotlib.pyplot as plt
import uuid
from queue import Queue


class Node:

    def __init__(self, key, color="skyblue", visited_order=0):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.visited_order = visited_order
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(
            node.id, color=node.color, label=node.val, visited_order=node.visited_order
        )
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, total_visited):
    tree = nx.DiGraph()
    pos = {}
    pos[tree_root.id] = (0, 0)
    tree = add_edges(tree, tree_root, pos)

    colors = [
        generate_color(node[1]["visited_order"], total_visited)
        for node in tree.nodes(data=True)
    ]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(12, 8))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def heap_to_tree(heap, index=0):
    if index < len(heap):
        node = Node(heap[index])
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        if left_index < len(heap):
            node.left = heap_to_tree(heap, left_index)
        if right_index < len(heap):
            node.right = heap_to_tree(heap, right_index)
        return node
    else:
        return None


def generate_color(index, total):
    intensity = 255 - int((index / total) * 255)
    return f"#0000{intensity:02x}"


def dfs(node, visited=None, order=0):
    if visited is None:
        visited = {}
    visited[node.id] = order
    node.visited_order = order
    order += 1
    if node.left:
        order = dfs(node.left, visited, order)
    if node.right:
        order = dfs(node.right, visited, order)
    return order


def bfs(root):
    order = 0
    visited = {}
    queue = Queue()
    queue.put((root, order))
    while not queue.empty():
        node, order = queue.get()
        if node.id not in visited:
            visited[node.id] = order
            node.visited_order = order
            order += 1
            if node.left:
                queue.put((node.left, order))
            if node.right:
                queue.put((node.right, order))
    return max(visited.values())


def reset_visited_order(node):
    if node is not None:
        node.visited_order = 0
        reset_visited_order(node.left)
        reset_visited_order(node.right)


heap = [1, 3, 5, 7, 9, 2, 4]
heapq.heapify(heap)
heap_tree = heap_to_tree(heap)

reset_visited_order(heap_tree)
total_visited_dfs = dfs(heap_tree)
draw_tree(heap_tree, total_visited_dfs)

reset_visited_order(heap_tree)
total_visited_bfs = bfs(heap_tree)
draw_tree(heap_tree, total_visited_bfs)
