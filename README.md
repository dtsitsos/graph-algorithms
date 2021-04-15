# graph-algorithms
this is a university project about graph theory algorithms problems using networkx library.

## q_a
At q_a we create a graph: Florentine Families Graph, we save it at gexf file and edge_list file, we display the grapf with default layout, we display the graph as planar and we display the graph with layout Kamada-Kawai.

## q_b
We find the node with the biggest betweenness centrality, the node with the biggest pagerank centrality, the node with the biggest closeness centrality and we calculate the average closeness centrality of the graph.

## q_c
**given: We assune that a biker can ride his bike with 80km/day. He can only stay at a town. He starts from Xanthi and wants to travel to all thw towns of Greece.**

We answer if this is possible and if not how many times he needs to use mass transit.

**given: We assume that he can ride his bicycle with maximum speed 120km/day.**

We find which is the shortest path to travel from Xanthi to Sparti. 
We find how many kms will travel if he goes to Patra via Motorway 1 or via Egnatia.
Finally, we find how many days he need to travel from Xanthito Patra via Motorway 1 or via Egnatia.

## q_d
**given: a company wants to lay cables alongside to road with maximum length of 120km. The goal is to connect all the towns of Greece.**

We find the best connections to achieve the least possible total length.

**note:** To solve this problem we use the algorithm of the removal of the maximum edges. More specifically we removed the biggest roads. As a result we have 1 graph where all its vertices are connected to each other with the minimum possible distance while at the same time the graph remains connected.
For more details about this method please contact me. 


