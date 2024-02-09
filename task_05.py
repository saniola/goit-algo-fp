import heapq
import networkx as nx
import matplotlib.pyplot as plt
import uuid


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, type):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(12, 8))
    nx.draw(
        tree,
        pos=pos,
        with_labels=False,
        arrows=False,
        node_size=2500,
        node_color=colors,
    )

    nx.draw_networkx_labels(tree, pos, labels, font_size=12)

    plt.text(
        0,
        max(pos.values(), key=lambda x: x[1])[1] + 0.5,
        f"{type} Traversal",
        fontsize=15,
        ha="center",
        va="center",
    )

    plt.title("Binary Tree Visualization", fontsize=20)
    plt.show()


def heap_to_tree(heap):
    heap_nodes = [Node(num) for num in heap]
    heapq.heapify(heap_nodes)

    while len(heap_nodes) > 1:
        node1 = heapq.heappop(heap_nodes)
        node2 = heapq.heappop(heap_nodes)
        merged_node = Node(node1.val + node2.val)
        merged_node.left = node1
        merged_node.right = node2
        heapq.heappush(heap_nodes, merged_node)

    return heap_nodes[0]


def generate_color(depth, type):
    factor = 50
    if type == "DFS":
        color_value = max(0, 255 - depth * factor)
        return f"#0000{color_value:02x}"
    else:
        color_value = max(0, 255 - depth * factor)
        return f"#00{color_value:02x}00"


def dfs(node, depth=0):
    if node is not None:
        node.color = generate_color(depth, "DFS")
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)


def bfs(node):
    queue = [(node, 0)]
    while queue:
        current_node, depth = queue.pop(0)
        current_node.color = generate_color(depth, "BFS")
        if current_node.left:
            queue.append((current_node.left, depth + 1))
        if current_node.right:
            queue.append((current_node.right, depth + 1))


nums = [5, 10, 14, 7, 3]
heapq.heapify(nums)

tree_root = heap_to_tree(nums)

dfs(tree_root)
draw_tree(tree_root, "Depth-First")

bfs(tree_root)
draw_tree(tree_root, "Breadth-First")
