
# homework 1 
# writing the psuedo code for them Spanish Rice Maze Problem


# creating a function to create the maze of size n and n^2 contents (N,E,W,S,NE,NW,SE,SW)

import numpy as np
from collections import deque as queue

#direction movement stored in array for row movement and column 
#creating matrix using a function:
def create():
    #input matrix size 
    size = int(input("enter the size of square matrix: \n"))
    maze = []
    for i in range (size):
        elements = list(map(str, input().split()))
        maze.append(elements) 
    return maze

# considering the [['E', 'S', 'SW'], ['E', 'NW', 'S'], ['N', 'E', 'F']] maze graph directions
#building the successor function 
def successor(cr,cc,matrix,successors,visited,path):
    
    #adding visited list
    #creating the range of movement 
    #if the direction is east the movement should only be lateral increment i.e. column + range(1 to (size of matrix))
    tsuc = []
    if (cr,cc) not in visited:
        visited.append((cr,cc))
        print(visited)

    if (cr,cc) not in path:
        path.append((cr,cc))
        print(path)

    if(matrix[cr][cc] == 'F'):
        return;

    if (matrix[cr][cc] == 'N'):
        for tr in range(1,len(matrix)):
          temp = cr - tr
          if temp in range (0,len(matrix)):
                #print(matrix[cr - tr][cc])
                print(cr-tr)
                successors.append(matrix[cr-tr][cc])
                tsuc.append(matrix[cr-tr][cc])
                if len(tsuc) == 0
                    tsuc.pop()


    if (matrix[cr][cc] == 'E'):
        for tc in range(1,len(matrix)):
            print(cc+tc)
            print(matrix[cr][cc+tc]) 
            successors.append(matrix[cr][cc+tc])
#----------------------------------------------------------

#main function
maze = create()
path = []
visited = []
successors = []
successor(1,0,maze,successors,visited)
print(successors)
