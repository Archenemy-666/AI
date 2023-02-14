
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
def successor(cr,cc,matrix,successors,visited):
# include path removed for now


    #adding visited list
    #creating the range of movement 
    #if the direction is east the movement should only be lateral increment i.e. column + range(1 to (size of matrix))
    # tsuc = []
    #if (cr,cc) not in visited:
    #    visited.append((cr,cc))
       # print(visited)
    #adding path to be explored
    #if (cr,cc) not in path:
    #    path.append((cr,cc))
    #    print(path)

    if(matrix[cr][cc] == 'F'):
        successors.append([cr,cc])
        #successors.append(matrix[cr][cc])
        return successors

    if (matrix[cr][cc] == 'N'):
        for tr in range(1,len(matrix)):
          north = cr - tr
          if north in range (0,len(matrix)):
                #print(matrix[cr - tr][cc])
               # print(cr-tr)
                #successors.append(matrix[north][cc])
                successors.append([north,cc])
                # tsuc.append(matrix[north][cc])
                #if not len(tsuc) == 0:
                   # path.append(cr,cc)

    if (matrix[cr][cc] == 'S'):
        for tr in range(1,len(matrix)):
            print(cr+tr)
            south = cr + tr
            if south in range (0,len(matrix)):
                successors.append([south,cc]) 
                #successors.append(matrix[south][cc])

    if (matrix[cr][cc] == 'E'):
        for tc in range(1,len(matrix)):
            east = cc+tc
            if east in range (0,len(matrix)):
               # print(matrix[cr][east]) 
                successors.append([cr,east]) # testing on converting list of location to location

    if (matrix[cr][cc] == 'W'):
        for tc in range(1,len(matrix)):
            west = (cc-tc)
            if west in range (0,len(matrix)):
               # print(matrix[cr][west]) 
                successors.append([cr,west])
                #successors.append(matrix[cr][west])

    if (matrix[cr][cc] == 'NE'):
        for tr in range(1,len(matrix)):
            #for tc in range(1,len(matrix)):
               # if(tr == tc):
                    northeastR = cr - tr
                    northeastC = cc + tr
                    if northeastR in range (0,len(matrix)) and northeastC in range (0,len(matrix)):
                        successors.append([northeastR,northEastC]) 
                        #successors.append(matrix[NorthEastR][NorthEastC])

    if (matrix[cr][cc] == 'NW'):
        for tr in range(1,len(matrix)):
            #for tc in range(1,len(matrix)):
               # if(tr == tc):
                    northwestR = cr - tr
                    northwestC = cc - tr
                    if northwestR in range (0,len(matrix)) and  northwestC in range (0,len(matrix)):
                        successors.append([northwestR,northwestC]) 
                        #successors.append(matrix[northwestR][northwestC])

    if (matrix[cr][cc] == 'SE'):
        for tr in range(1,len(matrix)):
           # for tc in range(1,len(matrix)):
                #if(tr == tc): # for only symmetric diagnol movement
                    southeastR = cr + tr
                    southeastC = cc + tr
                    if southeastR in range (0,len(matrix)) and southeastC in range (0,len(matrix)):
                        successors.append([southeastR,southeastC])
                        #successors.append(matrix[southeastR][southeastC])


    if (matrix[cr][cc] == 'SW'):
        for tr in range(1,len(matrix)):
            #for tc in range(1,len(matrix)):
                #if (tr == tc): # only diagnol movement not a unsymmetric diagnol
                    southwestR = cr + tr
                    southwestC = cc - tr
                    if southwestR in range (0,len(matrix)) and southwestC in range (0,len(matrix)):
                        #print(matrix[southwestR][southwestC])
                        #successors.append(matrix[southwestR][southwestC])
                        successors.append([southwestR,southwestC])        
                
def leafcheck(cr,cc,successors):
    if len(successor) == 0:
        return true

# this is important to convert the successors states from locations to values in maze
def convert(maze,successors):
    listl = []
    for i in successors:
        listl.append((maze[i[0]][i[1]]))
    return(listl)

#creating a depth first function
def dfs(cr,cc,maze,successors,visited):
    #adding current marker 
    current = ([cr,cc])
    if current in visited:
        print("hello")
        temp = successors.pop()
        print(successors)
        visited.append(temp)
        successor(temp[0],temp[1],maze,successors,visited)
    print(successors)
    child = successors.pop()
    dfs(child[0],child[1],maze,successors,visited)
    
#----------------------------------------------------------

#function to check if the child 


#main function
#initializing variables
maze = create()
path = []
visited = []
successors = []

dfs(0,0,maze,successors,visited)
#successor(0,0,maze,successors,visited)
#print(successors)

#templist = convert(maze,successors)
#print(templist)


