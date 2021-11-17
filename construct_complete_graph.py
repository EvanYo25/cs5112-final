import pandas as pd
import pprint

data = pd.read_csv('data/distance_matrix copy.txt', header = None)

data = data.replace(0, 10000)

# Test Read-In
# print(len(data))
# print(len(data[0]))
# print(data[0][0])
# print(type(data[0][0]))

subway_stops = {
    0:	"Rector St",
    1:	"WTC Cortlandt",
    2:	"Chambers St",
    3:	"Franklin Street Station",
    4:	"Canal St",
    5:	"Houston St",
    6:	"Christopher St Station",
    7:	"14 St",
    8:	"18 Street Station",
    9:	"23 St",
    10:	"28 St",
    11:	"34 Street - Penn Station",
    12:	"Times Sq - 42 St",
    13:	"50 Street Station",
    14:	"59 St - Columbus Circle",
    15:	"66 St-Lincoln Center",
    16:	"72 St",
    17:	"79 St",
    18:	"86 St",
    19:	"96 St",
    20:	"103 St",
    21:	"Cathedral Parkway 110 Street",
    22:	"116 Street Station - Columbia University",
    23:	"125 Street Station",
    24:	"137 St - City College",
    25: "145 St",
    26:	"157 Street Station",
    27:	"168 St - Washington Hts",
    28:	"191 Street",
    29:	"Dyckman St",
    30:	"207 St",
    31:	"215 Street Station",
    32:	"Harlem / 148 St",
    33:	"135 St",
    34:	"116 St",
    35:	"Central Park North (110 St)",
    36:	"Park Place",
    37:	"Fulton Street",
    38:	"Wall Street Station",
    39:	"116 Street",
    40:	"110 Street",
    41:	"103 Street Station",
    42:	"96 Street Station",
    43:	"86th Street",
    44:	"77 St",
    45:	"68 St-Hunter College",
    46:	"59 St-Lexington Av",
    47:	"51 St",
    48:	"Grand Central - 42 St",
    49:	"33 St",
    50:	"28 St Station",
    51:	"14 St - Union Sq",
    52:	"Astor Pl",
    53:	"Bleecker St",
    54:	"Spring Street",
    55:	"Brooklyn Bridge - City Hall",
    56:	"5 Av",
    57:	"34 Street-Hudson Yards Subway Station",
    58:	"207 St Station",
    59:	"190 St",
    60:	"181 St",
    61:	"175 St",
    62:	"168 St",
    63:	"163 Street Subway Station",
    64:	"155 St",
    65:	"145th St And St Nicholas Ave MTA Subway Station",
    66:	"125 St",
    67:	"59 St-Columbus Circle",
    68:	"42 St - Port Authority Bus Terminal",
    69:	"34 St - Penn Station",
    70:	"14 St / 8 Av",
    71:	"W 4 St - Wash Sq",
    72:	"Canal Street",
    73:	"Fulton Street Subway Station",
    74:	"Lexington Av/53 St",
    75:	"5 Avenue-53 St Station",
    76:	"7 Avenue Station",
    77:	"50 St",
    78:	"23rd St",
    79:	"Spring St.",
    80:	"World Trade Center",
    81:	"155 Street",
    82:	"135 Street",
    83:	"Cathedral Pkwy",
    84:	"81 Street - Museum of Natural History",
    85:	"47-50 Sts-Rockefeller Ctr",
    86:	"42 St-Bryant Park Station",
    87:	"34 St - Herald Sq Subway Station",
    88:	"Broadway-Lafayette St",
    89:	"Grand St",
    90:	"Roosevelt Island Subway Station",
    91:	"Lexington Av/63 St",
    92: "57 Street",
    93:	"23 St Station",
    94:	"14 St / 6 Av",
    95:	"2nd Avenue",
    96:	"Delancey St · Essex St",
    97:	"East Broadway",
    98:	"Broad St",
    99:	"Fulton St",
    100: "Bowery",
    101: "86th St",
    102: "City Hall Station",
    103: "Cortlandt St",
    104: "3 Av",
    105: "1 Av",
    106: "Whitehall St"
}


# Test Output
# start = 4
# print(start, "start", subway_stops[start])
# for i in range(len(data[start])):
#     if data[start][i] != 10000:
#         print(i, ':', subway_stops[i], "dist:", data[start][i])


class Graph:
    def minDistance(self,dist,queue):
        # Initialize min value and min_index as -1
        minimum = float("Inf")
        min_index = -1
        
        # from the dist array,pick one which has min value and is still in queue
        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index

    def printPath(self, parent, j):
        #Base Case : If j is source
        if parent[j] == -1 :
            print(subway_stops[j], j)
            return
        self.printPath(parent , parent[j])
        print(subway_stops[j], j)
		
    def printSolution(self, src, dist, parent, copy_set):
        # src = 0
        print("Vertex \t\tDistance from Source\tPath")
        for i in range(1, len(dist)):
            if i not in copy_set:
                continue
            print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i]))
            self.printPath(parent, i)

    def constructGraph(self, src, dist, parent, copy_set):
        def constructRoute(parent, j, route):
            if parent[j] == -1:
                # print(subway_stops[j], j)
                route.append(j)
                return route
            constructRoute(parent, parent[j], route)
            # print(subway_stops[j], j)
            route.append(j)
            return route
        ret = []
        retRoute = []
        for i in range(1, len(dist)):
            if i == src:
                ret.append(0)
                retRoute.append(constructRoute(parent, i, []))
            elif i not in copy_set:
                continue
            else:
                ret.append(dist[i])
                retRoute.append(constructRoute(parent, i, []))
        return ret, retRoute


    def dijkstra(self, graph, src, target_set):
        copy_set = target_set.copy()

        row = len(graph)
        col = len(graph[0])

        # The output array. dist[i] will hold
        # the shortest distance from src to i
        # Initialize all distances as INFINITE
        dist = [float("Inf")] * row

        #Parent array to store
        # shortest path tree
        parent = [-1] * row

        # Distance of source vertex
        # from itself is always 0
        dist[src] = 0

        # Add all vertices in queue
        queue = []
        for i in range(row):
            queue.append(i)
            
        #Find shortest path for all vertices
        while queue and len(target_set) > 0:

            # Pick the minimum dist vertex
            # from the set of vertices
            # still in queue
            u = self.minDistance(dist,queue)

            # remove min element	
            queue.remove(u)
            if u in target_set:
                target_set.remove(u)

            # Update dist value and parent
            # index of the adjacent vertices of
            # the picked vertex. Consider only
            # those vertices which are still in
            # queue
            for i in range(col):
                '''Update dist[i] only if it is in queue, there is
                an edge from u to i, and total weight of path from
                src to i through u is smaller than current value of
                dist[i]'''
                if graph[u][i] and i in queue:
                    if dist[u] + graph[u][i] < dist[i]:
                        dist[i] = dist[u] + graph[u][i]
                        parent[i] = u

        # self.printSolution(src, dist, parent, copy_set)
        return self.constructGraph(src, dist, parent, copy_set)

# g= Graph()
# arr = g.dijkstra(data, 3, {1, 2, 3, 4, 5, 6, 7, 8, 9})


def constructComplete(data, stations):
    ret = []
    retR = []
    for i in stations:
        g = Graph()
        a, b = g.dijkstra(data, i, set(stations))
        ret.append(a)
        retR.append(b)

    return ret, retR


# chosen_station = [1, 2, 8, 50, 4]
# chosen_station.sort()

# print(chosen_station)
# print("-------")

# complete_graph, route = constructComplete(data, chosen_station)

# pprint.pprint(complete_graph)
# pprint.pprint(route)