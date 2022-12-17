import networkx as nx
import matplotlib.pyplot as plt

# Задача 1

city_list = []
with open("cities.csv", "r") as file:
    while True:
        line = file.readline()
        if line:
            split = line.split(';')
            split[2] = int(split[2])
            city_list.append(split)
        else:
            break

g = nx.Graph()
for i in city_list:
    g.add_edge(i[0], i[1], weight=i[2])

pos = nx.spring_layout(g)
nx.draw_networkx(g, pos)
plt.title("Граф зі списку")
plt.show()

# Задача 2

def short_path(g):
    start = input("Where are you?\n")
    end = input("And where are you going?\n")
    route = nx.shortest_path(g, 'Poltava', 'Kyiv', weight='weight')
    dist = nx.shortest_path_length(g, 'Poltava', 'Kyiv', weight='weight')
    print("The best route is: ")
    print(*route, sep="-")
    print("and the distance is", dist)

short_path(g)