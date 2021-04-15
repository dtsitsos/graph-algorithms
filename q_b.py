import networkx as nx
import matplotlib.pyplot as plt

G = nx.florentine_families_graph()

#B-1
b = nx.betweennes_centrality(G)
bs = sorted(b.items(), reverse= True, key=lambda kv: kv[1]) #taxinomisi,se #fthinousa seira, apo kathe stoixeio tha pairnei to deftero melos
print(b)#mh taxinomhmena
print(bs)#taxinomhmena
print(bs[0])#pairnw etsi to prwto zevgari (prtwto stoixeio)

#B-2
c = nx.pagerank(G)
print("Node with maximum pagerank centrality: ", max(c, key = c.get))

#Β-3
e = nx.closeness_centrality(G)
print("Node with maximum closeness centrality: ", max(e, key = e.get))

#B-4
sum = e['Strozzi'] + e['Tornabuoni'] + e['Medici'] + e['Albizzi'] + e['Ridolfi'] + e['Pazzi'] + e['Acciaiuoli'] + e['Bischeri'] + e['Peruzzi'] + e['Salviati'] + e['Castellani'] + e['Lamberteschi'] + e['Ginori'] + e['Guadagni'] + e['Barbadori']
avg = sum / 15
print(“The Average value of closeness centrality is:”,avg)

