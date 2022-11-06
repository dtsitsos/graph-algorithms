import networkx as nx
import hellas_cities


#C1
D80 = hellas_cities.get_cities_distances_80_graph()
print('D80:', nx.info(D80))

#check if the graph is connnected: : Return True if the graph is connected, false otherwise.

print('Is D80 connected?', nx.is_connected(D80))

#poses fores tha hreiastei na dianysei --> posa tmhmata apoteleitai o grafos :psahnw connected components !!

print('How many times should he use means of transport, in order to reach his destination ?', nx.number_connected_components(D80)-1)

#C-2

#Ypologismos tou shortest_path apo Xanthi pros Sparti
H = hellas_cities.get_cities_distances_120_graph()
print('Shortest route from Xanthi to Sparti is: ', nx.shortest_path(H, source = 'Xanthi', target = 'Sparti'))

#C-3

#Sinartisi h opoia ypologizei thn apostash enos monopatiou
def path_length(G, path):
   total_distance = 0
   length = len(path)
   for hop in range (length-1):
       hop_distance = G[path[hop]][path[hop+1]]['weight']
       total_distance = total_distance + hop_distance
   return total_distance

#EGNATIA
EGNATIA_1 = nx.shortest_path(H, 'Xanthi', 'Ioannina')
EGNATIA_2 = nx.shortest_path(H, 'Ioannina', 'Patra')
EGNATIA = EGNATIA_1 + EGNATIA_2
length_egnatia = path_length(H,EGNATIA) #xhl. apostash egnatias

print('Egnatia length:', length_egnatia)

#PATHE
path1 = nx.shortest_path(H, 'Xanthi', 'Athina')
path2 = nx.shortest_path(H, 'Athina', 'Patra')

PATHE = path1 + path2 
length_pathe = path_length(H, PATHE) #xhl. apostash Pathe

print('pathe length:', length_pathe)

#C-4

#Synartisi upologismou ton hmerwn
def count_days(H, path):
   total_distance = 0
   days = 0
   length = len(path)
   for hop in range(length - 1):
       hop_distance = H[path[hop]][path[hop + 1]]['weight']
       total_distance = total_distance + hop_distance
       if total_distance > 120:
           days = 1 + days
           total_distance = hop_distance
   return days  

#Ypologismos hmerwn gia thn Egnatia
days_egnatia = count_days(H,EGNATIA)
print('Egnatia days:', days_egnatia)

#Ypologismos hmerwn gia Pathe
days_pathe = count_days(H,PATHE)
print('Pathe days:', days_pathe)
