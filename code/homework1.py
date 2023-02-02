# homework 1 
# writing the psuedo code for them Spanish Rice Maze Problem


# creating a function to create the maze of size n and n^2 contents (N,E,W,S,NE,NW,SE,SW)

import numpy as np

#creating matrix using a function:
def create():
    #input matrix size 
    size = int(input("enter the size of square matrix: \n"))
    
    maze = []
    for i in range (size):
        elements = list(map(str, input().split()))
        maze.append(elements) 
    return maze

#add values in matrix using rows and col
'''def buildMaze(blueprint):
    
    for __in rangeblueprint:
            temp = int(input("enter the value for the matrix: \n"))
            blueprint[col][row] = temp
    print()
'''
def North(loc,row,col):
    loc = 
    

maze = create()
print(maze)
#buildMaze(blueprint)
print(len(maze))

