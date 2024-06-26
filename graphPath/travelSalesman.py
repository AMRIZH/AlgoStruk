# Traveling Salesman Problem

import random
import math
import copy

class TravelSalesman:
    def __init__(self, cities, distanceMatrix):
        self.cities = cities
        self.distanceMatrix = distanceMatrix
        self.population = []
        self.populationSize = 10
        self.mutationRate = 0.1
        self.elitism = 0.1
        self.generations = 100
        self.bestDistance = 0
        self.bestPath = []
        self.createPopulation()
        self.calculateFitness()

    def createPopulation(self):
        for i in range(self.populationSize):
            path = self.cities[:]
            random.shuffle(path)
            self.population.append(path)

    def calculateFitness(self):
        for i in range(self.populationSize):
            distance = 0
            for j in range(len(self.population[i]) - 1):
                distance += self.distanceMatrix[self.population[i][j]][self.population[i][j + 1]]
            distance += self.distanceMatrix[self.population[i][-1]][self.population[i][0]]
            if self.bestDistance == 0 or distance < self.bestDistance:
                self.bestDistance = distance
                self.bestPath = self.population[i]
            self.population[i] = (self.population[i], 1 / distance)

    def crossover(self, parent1, parent2):
        child = []
        start = random.randint(0, len(parent1) - 1)
        end = random.randint(0, len(parent1) - 1)
        if start > end:
            start, end = end, start
        for i in range(start, end):
            child.append(parent1[i])
        for i in range(len(parent2)):
            if parent2[i] not in child:
                child.append(parent2[i])
        return child

    def mutate(self, path):
        if random.random() < self.mutationRate:
            index1 = random.randint(0, len(path) - 1)
            index2 = random.randint(0, len(path) - 1)
            path[index1], path[index2] = path[index2], path[index1]
        return path

    def evolve(self):
        newPopulation = []
        self.population.sort(key=lambda x: x[1], reverse=True)
        for i in range(int(self.populationSize * self.elitism)):
            newPopulation.append(self.population[i][0])
        for i in range(int(self.populationSize * (1 - self.elitism))):
            parent1 = self.population[random.randint(0, self.populationSize - 1)][0]
            parent2 = self.population[random.randint(0, self.populationSize - 1)][0]
            child = self.crossover(parent1, parent2)
            child = self.mutate(child)
            newPopulation.append(child)
        self.population = []
        for path in newPopulation:
            self.population.append((path, 1 / self.calculateDistance(path)))
            
    def calculateDistance(self, path):
        distance = 0
        for i in range(len(path) - 1):
            distance += self.distanceMatrix[path[i]][path[i + 1]]
        distance += self.distanceMatrix[path[-1]][path[0]]
        return distance
      
    def run(self):
        for i in range(self.generations):
            self.evolve()
            print("Generation", i + 1, "- Best distance:", self.bestDistance, "- Best path:", self.bestPath)
            
# Example usage:
cities = ['A', 'B', 'C', 'D']
distanceMatrix = {
    'A': {'A': 0, 'B': 2, 'C': 3, 'D': 1},
    'B': {'A': 2, 'B': 0, 'C': 2, 'D': 3},
    'C': {'A': 3, 'B': 2, 'C': 0, 'D': 2},
    'D': {'A': 1, 'B': 3, 'C': 2, 'D': 0}
}

ts = TravelSalesman(cities, distanceMatrix)

ts.run()

# Output:
# Generation 1 - Best distance: 7 - Best path: ['A', 'B', 'C', 'D']
