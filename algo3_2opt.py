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

MAXCOUNT = 100


def calDist(city_a, city_b):
    return complete_graph[city_b][city_a]

def calPathDist(indexList):
    sum = 0.0
    for i in range(1, len(indexList)):
        sum += calDist(indexList[i], indexList[i - 1])
    return sum    

def pathCompare(path1, path2):
    if calPathDist(path1) <= calPathDist(path2):
        return True
    return False
    
def generateRandomPath(bestPath):
    a = np.random.randint(len(bestPath))
    while True:
        b = np.random.randint(len(bestPath))
        if np.abs(a - b) > 1:
            break
    if a > b:
        return b, a, bestPath[b:a+1]
    else:
        return a, b, bestPath[a:b+1]
    
def reversePath(path):
    rePath = path.copy()
    rePath[1:-1] = rePath[-2:0:-1]
    return rePath
    
def updateBestPath(bestPath):
    count = 0
    while count < MAXCOUNT:
        # print(calPathDist(bestPath))
        # print(bestPath.tolist())
        start, end, path = generateRandomPath(bestPath)
        rePath = reversePath(path)
        
        if pathCompare(path, rePath):
            count += 1
            continue
        else:
            count = 0
            bestPath[start:end+1] = rePath
    return bestPath
    

def getExactPath(path):
    ret = []
    for i in path:
        ret.append(chosen_station[i])
    print(ret)
    return ret

def getPathWithName(exactPath):
    ret = []
    for i in exactPath:
        ret.append(subway_stops[i])
    print(ret)
    return ret

def printPathWithDetail(path):
    ret = []
    for i in range(len(path) - 1):
        pt = route[path[i]][path[i+1]]
        for j in pt:
            ret.append(subway_stops[j])
        if i != len(path) - 2:
            ret.pop()
    print(ret)

def opt2():
    # construct an array of 0~len(chosen_station)
    bestPath = np.arange(0, len(chosen_station))
    bestPath[0], bestPath[start_index] = bestPath[start_index], bestPath[0]

    # append the start node to end
    bestPath = np.append(bestPath, start_index)

    # run algorithm
    bestPath = updateBestPath(bestPath)


    print("result: ")
    print("distance: ", calPathDist(bestPath))
    print("best Path", bestPath)
  
    exactPath = getExactPath(bestPath)
    getPathWithName(exactPath)
    printPathWithDetail(bestPath)

opt2()