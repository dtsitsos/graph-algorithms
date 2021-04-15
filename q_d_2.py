import networkx as nx
import matplotlib.pyplot as plt
import hellas_cities

D120= hellas_cities.get_cities_distances_120_graph()

all_edges = D120.edges()


#******************number_of_edges************************
def number_of_edges(edges,city):
    count = 0
    for i in edges:
        if i[1] == city:
            count = count + 1
        if i[0] == city:
            count = count + 1
    count = count - 2
    return count
#*********************************************************

#********************find_max_edges***********************
def find_max_distance(all_edges,starting_dist):
    max_distance = 0 
    for y in all_edges:
        no_of_edges_1 = number_of_edges(all_edges,y[0])
        no_of_edges_2 = number_of_edges(all_edges,y[1])
        city_1 = y[0]
        city_2 = y[1]
        temp_distance = D120[city_1][city_2]['weight']
        if no_of_edges_1 > 1 and no_of_edges_2 > 1 and temp_distance > max_distance and temp_distance < starting_dist:
            max_distance = temp_distance
            max_dist = y
    return max_dist
#*********************************************************

#***********************remove_edge***********************
def remove_edge(edge):
    D120.remove_edge(edge[0],edge[1])
    final_edges = D120.edges()
    return final_edges
#*********************************************************

#********************final_connections********************

starting_dist = 200
while len(all_edges) > 77:
    edge_with_max_dist = find_max_distance(all_edges,starting_dist)
    temp_city_0 = edge_with_max_dist[0]
    temp_city_1 = edge_with_max_dist[1]
    temp_dist_city = D120[temp_city_0][temp_city_1]['weight']
    all_edges = remove_edge(edge_with_max_dist)
    if nx.is_connected(D120) == False:
        D120.add_edge(temp_city_0,temp_city_1,weight = temp_dist_city)
        starting_dist = temp_dist_city

#zeros
for j in all_edges: 
    if D120[j[0]][j[1]]['weight'] == 0:
        D120.remove_edge(j[0],j[1])

D120.remove_edge('Kozani','Florina')

all_edges = D120.edges()
#*********************************************************

#*********************final_distance**********************
final_distance = 0
for n in all_edges:
    final_distance = final_distance + D120[n[0]][n[1]]['weight']

#*********************************************************


print(all_edges)
print('The final distance of the graph is:',final_distance)
print(nx.info(D120))

nx.draw(D120, with_labels=True)
plt.show()
