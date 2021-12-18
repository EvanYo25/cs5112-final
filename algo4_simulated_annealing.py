import math                         #  math
import random                       #  random
import pandas as pd                 #  pandas  pd
import numpy as np                  #  numpy  np YouCans
import matplotlib.pyplot as plt     #  matplotlib.pyplot  plt
from construct_complete_graph import *

# print(subway_stops[0])
# print(type(data[0][1]))

# chosen_station = [12, 57, 86, 88, 90]
# chosen_station = [2, 7, 10, 13, 16, 22, 24, 45, 52, 54, 60, 68, 73, 75, 76, 84, 85, 86, 99, 106]
chosen_station = [1, 2, 3, 4, 6, 7, 8, 10, 13, 15, 16, 17, 18, 22, 24, 26, 27, 30, 33, 41, 42, 43, 45, 48, 51, 52, 54, 59, 60, 61, 63, 66, 68, 71, 73, 75, 76, 78, 79, 84, 85, 86, 89, 92, 93, 94, 99, 100, 102, 106]

# np.random.seed(0)
# stops = list(range(107))
# chosen_station = np.random.choice(stops, 20, replace=False)
# print("The chosen stations are:")
# print(chosen_station)
# chosen_station = chosen_station.tolist()

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

initTemp = 0
mark = 0

def initParameter():
    # custom function initParameter():
    # Initial parameter for simulated annealing algorithm
    tInitial = 2500.0                # (initial temperature)
    tFinal  = 1                     # (stop temperature)
    nMarkov = 3000                # Markov
    alfa    = 0.98                 # T(k)=alfa*T(k-1)

    global initTemp
    global mark
    initTemp = tInitial
    mark = nMarkov
    return tInitial,tFinal,alfa,nMarkov

# TSPLib
def read_TSPLib(fileName):
    # custom function read_TSPLib(fileName)
    # Read datafile *.dat from TSPlib
    # return coordinates of each city by YouCans, XUPT

    res = []
    with open(fileName, 'r') as fid:
        for item in fid:
            if len(item.strip())!=0:
                res.append(item.split())

    loadData = np.array(res).astype('int')      # i Xi Yi
    coordinates = loadData[:,1::]
    return coordinates

# def getDistMat(nCities, coordinates):
#     # custom function getDistMat(nCities, coordinates):
#     # computer distance between each 2 Cities
#     distMat = np.zeros((nCities,nCities))       # 
#     for i in range(nCities):
#         for j in range(i,nCities):
#             # np.linalg.norm   ij 
#             distMat[i][j] = distMat[j][i] = round(np.linalg.norm(coordinates[i]-coordinates[j]))
#     print(distMat)
#     print(distMat.shape)
#     return distMat   

def getDistMat():
    distMat = np.array(complete_graph)
    print(distMat)
    print(distMat.shape)
    return distMat
                           # 

#  TSP 
def calTourMileage(tourGiven, nCities, distMat):
    # custom function caltourMileage(nCities, tour, distMat):
    # to compute mileage of the given tour
    mileageTour = distMat[tourGiven[nCities-1], tourGiven[0]]   # dist((n-1),0)
    for i in range(nCities-1):                                  # dist(0,1),...dist((n-2)(n-1))
        mileageTour += distMat[tourGiven[i], tourGiven[i+1]]
    return round(mileageTour) 

 
def mutateSwap(tourGiven, nCities):
    # custom function mutateSwap(nCities, tourNow)
    # produce a mutation tour with 2-Swap operator
    # swap the position of two Cities in the given tour

    #  [0,n)  2 i,j
    i = np.random.randint(nCities)          #  [0,n) 
    while True:
        j = np.random.randint(nCities)      #  [0,n) 
        if i!=j: break                      #  i, j 

    tourSwap = tourGiven.copy()             #  tourSwap
    tourSwap[i],tourSwap[j] = tourGiven[j],tourGiven[i] #   i  j 

    return tourSwap

def adjustPath(path):
    ret = path.tolist()
    start_idx = chosen_station.index(start_station)

    round = ret.index(start_idx)
    for _ in range(round):
        ret.append(ret[0])
        ret = ret[1:]
    ret.append(ret[0])
    print(start_idx)
    print(round)
    print(ret)
    return ret

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

def main():
    tInitial,tFinal,alfa,nMarkov = initParameter()

    # nCities = coordinates.shape[0]
    nCities = len(chosen_station)
    print("nCities", nCities)
    # distMat = getDistMat(nCities, coordinates) 
    distMat = getDistMat()
    nMarkov = nCities                           # Markov 
    tNow    = tInitial                          #  (current temperature)

    # 
    tourNow   = np.arange(nCities)   # 01n 
    print("tourNow", tourNow)
    valueNow  = calTourMileage(tourNow,nCities,distMat) #  valueNow
    tourBest  = tourNow.copy()                          #  tourNow
    valueBest = valueNow                                #  valueNow
    recordBest = []
    recordNow  = []

    iter = 0
    while tNow >= tFinal:
        for k in range(nMarkov):    # Markov
            tourNew = mutateSwap(tourNow, nCities)
            # tourNew,deltaE = mutateSwapE(tourNow,nCities,distMat)   #    deltaE
            valueNew = calTourMileage(tourNew,nCities,distMat) # 
            deltaE = valueNew - valueNow

            #  Metropolis 
            if deltaE < 0:
                accept = True
                if valueNew < valueBest:
                    tourBest[:] = tourNew[:]
                    valueBest = valueNew
            else:
                pAccept = math.exp(-deltaE/tNow)
                if pAccept > random.random():
                    accept = True
                else:
                    accept = False

            if accept == True:
                tourNow[:] = tourNew[:]
                valueNow = valueNew

        #  0,n-1
        tourNow = np.roll(tourNow,2)

        recordBest.append(valueBest)
        recordNow.append(valueNow)
        print('i:{}, t(i):{:.2f}, valueNow:{:.1f}, valueBest:{:.1f}'.format(iter,tNow,valueNow,valueBest))

        iter = iter + 1
        tNow = tNow * alfa                              # T(k)=alfa*T(k-1)


    print("Tour verification successful!")
    print("Best tour: \n", tourBest)
    print("Best value: {:.1f}".format(valueBest))
  
    bestPath = adjustPath(tourBest)

    exactPath = getExactPath(bestPath)
    getPathWithName(exactPath)
    printPathWithDetail(bestPath)

    return recordBest

    exit()

if __name__ == '__main__':
    result = main()
    print(result)
    
    plt.plot(result, 'r')   # red line without marker
    plt.xlim([0, len(result)])
    plt.ylim([min(result)-5, max(result)+5])
    plt.title('sa - ' + str(len(chosen_station)) + 'stations, initial temperature ' + str(initTemp) + ',nMarkov ' + str(mark),fontsize=12)
    plt.xlabel('iteration',fontsize=10)
    plt.ylabel('distance',fontsize=10)
    plt.show()