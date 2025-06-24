""" 
Дейкстри для знаходження найкоротших шляхів у зваженому графі, 
використовуючи бінарну купу. Завдання включає створення графа, 
використання піраміди для оптимізації вибору вершин 
та обчислення найкоротших шляхів від початкової вершини до всіх інших.
"""

import networkx as nx
import matplotlib.pyplot as plt
import heapq 

# Граф у вигляді словника
G = nx.Graph()
G.add_edge("A", "B", weight=1)
G.add_edge("B", "C", weight=2)
G.add_edge("C", "D", weight=3)
G.add_edge("B", "E", weight=3)
G.add_edge("E", "C", weight=3)

def dijkstra_heap(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_distance == float ( 'infinity' ):
            break
        
        for source, destination in list(graph.edges(current_vertex)):
            weight = graph.edges[source,destination]['weight']
            print('Source: ' + source, ' -> Destination: ' + destination, '/ Weight: ' + str(weight))
            
            distance = current_distance + weight

            # If the new distance is shorter, then update the shortest path 
            if distance < distances[destination]:
                distances[destination] = distance
                heapq.heappush(priority_queue,(distance, destination))
                        

    return distances


# Використання алгоритму Дейкстри
shortest_paths = dijkstra_heap(G, "A")
print(shortest_paths)

# Візуалізація графа
pos = nx.spring_layout(G)  # Positions for all nodes
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, width=2)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

plt.axis("off")
plt.show()
