import uuid

import networkx as nx
import matplotlib.pyplot as plt

import heapq

class Node:
    def __init__(self, key, color = "skyblue" ):
        self.left = None
        self.right = None
        self.val = key
        self.color = color # Additional argument to store the node color
        self.id = str(uuid.uuid4()) # Unique identifier for each node

def add_edges(graph, node, pos, x =0, y =0, layer =1):
    if node is not None:
        graph.add_node(node.id, color =node.color, label =node.val) # Using id and storing node value
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x =l, y =y - 1, layer =layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x =r, y =y - 1, layer =layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1][ 'color' ] for node in tree.nodes( data = True )]
    labels = {node[0]: node[1][ 'label' ] for node in tree.nodes( data = True )} # Use node values ​​for labels

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos =pos, labels =labels, arrows = False , node_size =2500, node_color =colors)
    plt.show()

# Creating a tree
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Tree display
draw_tree(root)

#Heap example
numbersHeap = [ 4 , 10 , 3 , 5 , 1, 11, 23,17, 88 ]
heapq.heapify(numbersHeap)
print (numbersHeap)   # Output: [1, 4, 3, 5, 10]

def heap_to_tree(heap, index):
    if index >= len(heap):
        return None
    
    node = Node(heap[index])
    node.left = heap_to_tree(heap, 2 * index + 1)
    node.right = heap_to_tree(heap, 2 * index + 2)
    
    return node

t = heap_to_tree(numbersHeap,0)
# Tree display
draw_tree(t)