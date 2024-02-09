import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt


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
        # Use id and store the value of the node
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


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    # Use node value for labels
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
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


nums = [5, 10, 14, 7, 3]
heapq.heapify(nums)

heap_tree = heap_to_tree(nums)

# Display the tree
draw_tree(heap_tree)
