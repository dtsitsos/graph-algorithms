import networkx as nx
import matplotlib.pyplot as plt
import statistics
import hellas_cities

D120 = hellas_cities.get_cities_distances_120_graph()

all_edges = sorted(D120.edges(data = True), key = lambda t : -t[2]['weight'])

for edge in all_edges:
    D120.remove_edge(edge[0], edge[1])
    if( nx.number_connected_components(D120) > 1):
        D120.add_edge(edge[0], edge[1])
    
nx.draw_kamada_kawai(D120, with_labels = True)
plt.show()