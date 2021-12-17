import numpy as np
from construct_complete_graph import *

# print(subway_stops[0])
# print(type(data[0][1]))

chosen_station = [12, 57, 86, 88, 90]
chosen_station.sort()

start_station = 12
start_index = chosen_station.index(start_station)

print("chosen_station: ", chosen_station)
print("-------")

print("start_station: ", start_station)
print("-------")

complete_graph, route = constructComplete(data, chosen_station)

print("complete_graph:")
pprint.pprint(complete_graph)
print("------")

print("route between stations:")
pprint.pprint(route)
print("------")