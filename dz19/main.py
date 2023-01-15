import csv

with open('cities.csv') as f:
    reader = csv.reader(f)
    list = []
    for row in reader:
        list.append(row)
    print(list)

import networkx as nx
import matplotlib.pyplot as plt


edgelist = [['Ochakiv;Odesa;93'], ['Odesa;Voznesensk;140'], ['Voznesensk;Odesa;140']]


g = nx.Graph()
for edge in edgelist:
    g.add_edge(edge[0], edge[1], weight = edge[2])


pos = nx.spring_layout(g)
nx.draw_networkx(g, pos)
plt.title("Random Graph Generation Example")
plt.show()

nx.draw_networkx(g)



