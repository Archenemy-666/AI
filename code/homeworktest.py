def successor(cr,cc,matrix):
    successors = []
    steps = 0
    if (matrix[cr][cc] == 'N'):
        for tr in range(1,len(matrix)):
            north = cr - tr
            steps += 1 
            if north in range (0,len(matrix)):
                successors.append(([north,cc],steps))

    if (matrix[cr][cc] == 'S'):
        for tr in range(1,len(matrix)):
            south = cr + tr
            steps += 1
            if south in range (0,len(matrix)):
                successors.append(([south,cc],steps)) 
                #successors.append(matrix[south][cc])

    if (matrix[cr][cc] == 'E'):
        for tc in range(1,len(matrix)):
            east = cc+tc
            steps += 1
            if east in range (0,len(matrix)):
               # print(matrix[cr][east]) 
                successors.append(([cr,east], steps)) # testing on converting list of location to location

    if (matrix[cr][cc] == 'W'):
        for tc in range(1,len(matrix)):
            west = (cc-tc)
            steps += 1
            if west in range (0,len(matrix)):
               # print(matrix[cr][west]) 
                successors.append(([cr,west],steps))
                #successors.append(matrix[cr][west])

    if (matrix[cr][cc] == 'NE'):
        for tr in range(1,len(matrix)):
            #for tc in range(1,len(matrix)):
               # if(tr == tc):
                    northeastR = cr - tr
                    northeastC = cc + tr
                    steps += 1
                    if northeastR in range (0,len(matrix)) and northeastC in range (0,len(matrix)):
                        successors.append(([northeastR,northEastC],steps)) 
                        #successors.append(matrix[NorthEastR][NorthEastC])

    if (matrix[cr][cc] == 'NW'):
        for tr in range(1,len(matrix)):
            #for tc in range(1,len(matrix)):
               # if(tr == tc):
                    northwestR = cr - tr
                    northwestC = cc - tr
                    steps += 1
                    if northwestR in range (0,len(matrix)) and  northwestC in range (0,len(matrix)):
                        successors.append(([northwestR,northwestC], steps)) 
                        #successors.append(matrix[northwestR][northwestC])

    if (matrix[cr][cc] == 'SE'):
        for tr in range(1,len(matrix)):
           # for tc in range(1,len(matrix)):
                #if(tr == tc): # for only symmetric diagnol movement
                    southeastR = cr + tr
                    southeastC = cc + tr
                    steps += 1
                    if southeastR in range (0,len(matrix)) and southeastC in range (0,len(matrix)):
                        successors.append(([southeastR,southeastC],steps))
                        #successors.append(matrix[southeastR][southeastC])


    if (matrix[cr][cc] == 'SW'):
        for tr in range(1,len(matrix)):
            #for tc in range(1,len(matrix)):
                #if (tr == tc): # only diagnol movement not a unsymmetric diagnol
                    southwestR = cr + tr
                    southwestC = cc - tr
                    steps += 1
                    if southwestR in range (0,len(matrix)) and southwestC in range (0,len(matrix)):
                        #successors.append(matrix[southwestR][southwestC])
                        successors.append(([southwestR,southwestC],steps))
    return successors

def create():
    #input matrix size 
    size = int(input("enter the size of square matrix: \n"))
    maze = []
    for i in range (size):
        elements = list(map(str, input().split()))
        maze.append(elements) 
    return maze

def dfs(cr,cc,maze):
    start = ([cr,cc])
    visited = []
    stack  = [(start,[start], 0)]
    while stack:
        curr , path , cost = stack.pop()
        print(curr)
        if curr in visited:
            continue
        visited.append(curr)
        if (maze[curr[0]][curr[1]]) == 'F':
            return path, (len(path)-1)
        for next_pos, next_steps in successor(curr[0],curr[1],maze):
            stack.append((next_pos, path + [next_pos], cost + next_steps))
    return [],(len(path)-1)


def bfs(cr,cc,maze):
    start2 = ([cr,cc])
    visited2 = []
    queue = [[start2,0]]
    while queue:
        current = queue.pop(0)
        print (current)
        if current in visited2:
            continue
        if (maze[current[0]][current[1]]) == 'F':
            return True
        for neighbor,cost in successor(current[0],current[1],maze):
            print(neighbor:1)
    return False



        #if maze[[curr[0]][curr[1]] == 'F':
        #    print(path)
        #for neighour,next_step in successor(curr[0],curr[1],maze):
        #    queue.append((neighbor, path + [neighbor], cost))
    #return [],(len(path)-1)





#------------------------------main--------------------------------
from collections import defaultdict 
maze = create()
print(dfs(0,0,maze))
print("--------------------------------------- ")
bfs(0,0,maze)
