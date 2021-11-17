from construct_complete_graph import *

print(subway_stops[0])
print(type(data[0][1]))

chosen_station = [12, 57, 86, 88, 90]
chosen_station.sort()

print(chosen_station)
print("-------")

complete_graph, route = constructComplete(data, chosen_station)

pprint.pprint(complete_graph)
pprint.pprint(route)

