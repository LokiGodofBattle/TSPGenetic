import pygame
import numpy as np
import GeneticAlgorithm as ga
import math
from matplotlib import pyplot as plt
from GeneticAlgorithm import bestEver

pygame.init()

win = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Genetic TSP")

ellipseSize = 30
lineWidth = 3

run = True

reached = False

progress = []


plt.ylabel("Distance")
plt.xlabel("Generation")

clock = pygame.time.Clock()

while run:
    #pygame.time.delay(100)
    
    clock.tick()
    fps = clock.get_fps()
    if(fps != 0):
        print("Frametime: " + str((1000/fps)))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    win.fill((0, 0, 0))
    
    ga.calculateFitness()
    ga.normalizeFitness()    
    ga.nextGeneration()
    
    print("Beste Distanz: " + str(ga.distRecord))
    progress.append(ga.distRecord)

    #if ga.distRecord <= 7450 and not reached:
    #    print("NN Record Eingeholt! Generation: " + str(len(progress)))
    #   reached = True
        
    #if len(progress) >= 1000:
    #    pygame.time.delay(100000)

    plt.plot(progress)
    plt.pause(0.05)

    
    for i in range(0, ga.bestEver.size):
        pointA = ga.cities[int(ga.bestEver[i])]
        
        if(i != 0):
            pointB = ga.cities[int(ga.bestEver[i-1])]
            pygame.draw.line(win, (255, 255, 255), pointA, pointB, lineWidth)
        else:
            pointB = ga.cities[int(ga.bestEver[ga.bestEver.size-1])]
            pygame.draw.line(win, (255, 255, 255), pointA, pointB, lineWidth)
               
        rect = [pointA[0] - ellipseSize/2, pointA[1]-ellipseSize/2, ellipseSize, ellipseSize]
        pygame.draw.ellipse(win, (255, 255, 255), rect)
    
    pygame.display.update();