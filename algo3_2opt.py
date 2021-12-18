import numpy as np
import matplotlib.pyplot as plt
from construct_complete_graph import *

# print(subway_stops[0])
# print(type(data[0][1]))


# chosen_station = [12, 57, 86, 88, 90]

np.random.seed(0)
stops = list(range(107))
chosen_station = np.random.choice(stops, 50, replace=False)
print("The chosen stations are:")
print(chosen_station)
chosen_station = chosen_station.tolist()


chosen_station.sort()
start_station = chosen_station[0]
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
    
def updateBestPath(bestPath, MAXCOUNT):
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
    # print(ret)
    return ret

def getPathWithName(exactPath):
    ret = []
    for i in exactPath:
        ret.append(subway_stops[i])
    # print(ret)
    return ret

def printPathWithDetail(path):
    ret = []
    for i in range(len(path) - 1):
        pt = route[path[i]][path[i+1]]
        for j in pt:
            ret.append(subway_stops[j])
        if i != len(path) - 2:
            ret.pop()
    # print(ret)

def opt2(cnt):
    MAXCOUNT = cnt

    # construct an array of 0~len(chosen_station)
    bestPath = np.arange(0, len(chosen_station))
    bestPath[0], bestPath[start_index] = bestPath[start_index], bestPath[0]

    # append the start node to end
    bestPath = np.append(bestPath, start_index)

    # run algorithm
    bestPath = updateBestPath(bestPath, MAXCOUNT)


    # print("result: ")
    ret = calPathDist(bestPath)
    # print("distance: ", ret)
    # print("best Path", bestPath)
  
    exactPath = getExactPath(bestPath)
    getPathWithName(exactPath)
    printPathWithDetail(bestPath)

    return ret

if __name__ == '__main__':
    epoch = 2000
    x = range(1, epoch+1)
    result = []
    
    for i in x:
        if i%100 == 0:
            print(i)
        result.append(opt2(i))

    print(x)
    print(chosen_station)
    print(result)

    plt.plot(x, result, 'r')   # red line without marker
    plt.xlim([1, epoch+1])
    plt.ylim([min(result)-5, max(result)+5])
    plt.title('2opt - ' + str(len(chosen_station)) + 'stations, maxCount 1~' + str(epoch),fontsize=12)
    plt.xlabel('maxCount',fontsize=10)
    plt.ylabel('distance',fontsize=10)
    plt.show()