"""
Використовуючи код із завдання 4 для побудови бінарного дерева,
 створити програму на Python, яка візуалізує обходи дерева: у глибину та в ширину.
повинна відображати кожен крок у вузлах з різними кольорами, 
використовуючи 16-систему RGB (приклад #1296F0).
Кольори вузлів мають змінюватися від темних до світлих відтінків, залежно від послідовності обходу. 
Кожен вузол при його відвідуванні має отримувати унікальний колір, який візуально відображає порядок обходу.
    """
    
import uuid

import networkx as nx
import matplotlib.pyplot as plt

from collections import deque
import random




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
#draw_tree(root)


def random_color():
    return "#{:06X}".format(random.randint(0, 0xFFFFFF))


def bfs_iterative(graph, start):
    visited = set()
    queue = deque([start])
    colorIndex = 160


    while queue:  
        vertex = queue.popleft()
        if vertex not in visited and vertex is not None:
            print(vertex.val, end="\n")
            colorIndex = colorIndex-20
            vertex.color = f"#1297F0{hex(colorIndex)[2:]}"
            visited.add(vertex)
            queue.extend({vertex.left})
            queue.extend({vertex.right})
    return visited  


visited_nodes = bfs_iterative(root, root)
draw_tree(root)

def  dfs_iterative ( graph, start ):
    visited = set ()
    stack = [start]
    colorIndex = 160
    
    while stack:
        vertex = stack.pop() 
        if vertex not  in visited and vertex is not None:
            print (vertex, end= ' ' )
            colorIndex = colorIndex-20
            vertex.color = f"#1297F0{hex(colorIndex)[2:]}"
            stack.extend(([vertex.right]))  
            stack.extend(([vertex.left]))  
            
visited_nodes = dfs_iterative(root, root)
draw_tree(root)