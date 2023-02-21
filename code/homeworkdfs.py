def successor(cr,cc,matrix,successors):

    if (matrix[cr][cc] == 'N'):
        for tr in range(1,len(matrix)):
          north = cr - tr
          if north in range (0,len(matrix)):
                successors.append([north,cc])

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
                        print(matrix[southwestR][southwestC])
                        #successors.append(matrix[southwestR][southwestC])
                        successors.append([southwestR,southwestC])
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
    successors = []
    successors.append(start)
    while successors:
        curr = successors.pop()
        path = curr
        print(curr)
        if curr in visited:
            continue
        visited.append(curr)
        print(maze[curr[0]][curr[1]])
        if (maze[curr[0]][curr[1]]) == 'F':
            return 
        print(successor(curr[0],curr[1],maze,successors))
        for i in (successor(curr[0],curr[1],maze,successors)):
            print (path + [i])
    return False
 
#-------------------------- main --------------------------------------------------

maze = create()
x = dfs(0,0,maze)
print(x)
