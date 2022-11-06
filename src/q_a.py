import networkx as nx
import matplotlib.pyplot as plt

#A-1
G = nx.florentine_families_graph()

#A-2
nx.write_gexf(G,'florentine_families')

#A-3
G = nx.read_gexf('florentine_families')
nx.write_edgelist(G, 'florentine_families')

#A-4
nx.draw(G)
plt.show()

#A-5
nx.draw_planar(G)
plt.show()

#Α-6
nx.draw_kamada_kawai(G, with_labels = True)
plt.show()
