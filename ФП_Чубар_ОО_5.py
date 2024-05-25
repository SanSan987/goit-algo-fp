import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, title="Tree"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title(title)
    plt.show()

# Функція генерування кольорів з використанням 16-системи RGB
def generate_colors(n):
    colors = []
    for i in range(n):
        shade = int(255 * (i / (n - 1)))  # Від темних до світлих
        hex_color = "#{:02x}{:02x}{:02x}".format(shade, 0, 255 - shade)
        colors.append(hex_color)
    return colors

def inorder_traversal(root):  # Обхід дерева в глибину
    result = []
    if root:
        result += inorder_traversal(root.left)
        result.append(root)
        result += inorder_traversal(root.right)
    return result

def bfs_traversal(root):  # Обхід дерева в ширину
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

# Функція застосування кольорів до вузлів залежно до послідовності обходу
def apply_colors(nodes, colors):
    for node, color in zip(nodes, colors):
        node.color = color

def array_to_heap(arr):
    if not arr:
        return None
    nodes = [Node(key) for key in arr]
    for i in range(len(arr)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(arr):
            nodes[i].left = nodes[left_index]
        if right_index < len(arr):
            nodes[i].right = nodes[right_index]
    return nodes[0]

# Приклад масиву для створення бінарної купи
heap_array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Створення бінарної купи з масиву
heap_root = array_to_heap(heap_array)

# Візуалізація обходу в глибину (in-order traversal)
inorder_nodes = inorder_traversal(heap_root)
inorder_colors = generate_colors(len(inorder_nodes))
apply_colors(inorder_nodes, inorder_colors)
draw_tree(heap_root, title="In-order Traversal")

# Візуалізація обходу в ширину (breadth-first traversal)
heap_root = array_to_heap(heap_array)  # Відновлення кольорів
bfs_nodes = bfs_traversal(heap_root)
bfs_colors = generate_colors(len(bfs_nodes))
apply_colors(bfs_nodes, bfs_colors)
draw_tree(heap_root, title="Breadth-first Traversal")
