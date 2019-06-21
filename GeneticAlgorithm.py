import numpy as np
import random
import math
from math import floor

populationSize = 500
totalCities = 50
mutationRate = 0.1

export = False

distRecord = math.inf

cities = np.zeros((totalCities, 2))
    
order = np.zeros(totalCities)
    
population = np.zeros((populationSize, totalCities))
    
fitness = np.zeros((populationSize, 2))
    
bestEver = np.zeros(totalCities)

distances = np.zeros((totalCities, totalCities))

for i in range(0, totalCities):
    a = [random.randint(0, 1280), random.randint(0, 720)]
    cities[i] = np.asarray(a)
    order[i] = i

for i in range(0, populationSize):
    np.random.shuffle(order)
    population[i] =  np.copy(order)

for i in range(0, totalCities):
    for j in range(0, totalCities):
        distances[i, j] = np.linalg.norm(cities[i]-cities[j])        

if export:
    np.savetxt("Distance Matrix.txt", distances, delimiter=" ")
    np.savetxt("Cities.txt", cities, delimiter=" ")
    print("fertig!")
else:
    distances = np.loadtxt("50KnotenDM.txt", delimiter=" ")
    cities = np.loadtxt("50KnotenKO.txt", delimiter = " ")

def calcDistance(points, order):
    totalDist = 0
    for i in range(order.size):
        if (i < order.size-1):
                    cityAIndex = order[i]
                    cityBIndex = order[i+1]
                    totalDist += distances[int(cityAIndex), int(cityBIndex)]
        else:
                    cityAIndex = order[i]
                    cityBIndex = order[0]
                    totalDist += distances[int(cityAIndex), int(cityBIndex)]
    
    return totalDist


def calculateFitness():
    
    global bestEver
    
    for i in range(0, populationSize-1):
        dist = calcDistance(cities, population[i])
        global distRecord
        if(dist < distRecord):
            distRecord = dist
            bestEver = population[i]
        fitness[i] = [1 / (dist+1), i]

def normalizeFitness():
    fitnessSum = 0
    
    global populationSize
    global fitness
    
    for i in range(0, populationSize):
        fitnessSum += fitness[i][0]
    
    for i in range(0, populationSize):
        fitness[i][0] = fitness[i][0] / fitnessSum

    fitness = fitness[fitness[:,0].argsort()]

def nextGeneration():
    global population
    global totalCities
    
    children = []
    length = len(population)
    
    for i in range(0, length):
        parant1 = fitness[int(math.fabs(math.floor(np.random.normal(0, 0.1)*populationSize)))][0]
        parant2 = fitness[int(math.fabs(math.floor(np.random.normal(0, 0.1)*populationSize)))][0]
        
        child = crossOver(population[int(parant1)], population[int(parant2)])
        mutate(child, mutationRate)
        children.append(child)
    
    for i in range(0, 5):
        children[i] = bestEver
    
    population = np.asanyarray(children)
    
def mutate(someList, mutateRate):
    if random.random() < mutateRate:
        indexA = random.randint(0, totalCities-1)
        indexB = random.randint(0, totalCities-1)
        
        swap(someList, indexA, indexB)

def swap(someList, x, y):
    save = someList[x]
    someList[x] = someList[y]
    someList[y] = save


def crossOver(orderA, orderB):
    
    slice = []
    slice2 = []
    slice3 = []
    
    geneA = int(random.random() * len(orderA))
    geneB = int(random.random() * len(orderB))
    
    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        slice2.append(orderA[i])
        
    slice3 = [item for item in orderB if item not in slice2]

    slice = slice2 + slice3
    
    return slice

    
    
    
    
    
    
    
    