def successor(cr,cc,matrix,flip):
    successors = []
    steps = 0
    if flip == True:
        flip = False
        if (matrix[cr][cc] == 'N'):
            for tr in range(1,len(matrix)):
                south = cr + tr
                steps += 1
                if south in range (0,len(matrix)):
                    successors.append(([south,cc,flip],steps)) 
                    #successors.append(matrix[south][cc])
        
        if(matrix[cr][cc] == 'S'):
            for tr in range(1,len(matrix)):
                north = cr - tr
                steps += 1 
                if north in range (0,len(matrix)):
                    successors.append(([north,cc,flip],steps))
        
        if(matrix[cr][cc] == 'E'):
            for tc in range(1,len(matrix)):
                west = (cc-tc)
                steps += 1
                if west in range (0,len(matrix)):
                    successors.append(([cr,west,flip],steps))
        
        if(matrix[cr][cc] == 'W'):
            for tc in range(1,len(matrix)):
                east = cc+tc
                steps += 1
                if east in range (0,len(matrix)):
               # print(matrix[cr][east]) 
                    successors.append(([cr,east,flip], steps))
            
        if(matrix[cr][cc] == 'NE'):
            for tr in range(1,len(matrix)):
                southwestR = cr + tr
                southwestC = cc - tr
                steps += 1
                if southwestR in range (0,len(matrix)) and southwestC in range (0,len(matrix)):
                    successors.append(([southwestR,southwestC,flip],steps))
        
        if(matrix[cr][cc] == 'NW'):
            for tr in range(1,len(matrix)):
                southeastR = cr + tr
                southeastC = cc + tr
                steps += 1
                if southeastR in range (0,len(matrix)) and southeastC in range (0,len(matrix)):
                    successors.append(([southeastR,southeastC,flip],steps))

        if(matrix[cr][cc] == 'SE'):
            for tr in range(1,len(matrix)):
                northwestR = cr - tr
                northwestC = cc - tr
                steps += 1
                if northwestR in range (0,len(matrix)) and  northwestC in range (0,len(matrix)):
                    successors.append(([northwestR,northwestC,flip], steps)) 
            
        if(matrix[cr][cc] == 'SW'):
            for tr in range(1,len(matrix)):
                northwestR = cr - tr
                northwestC = cc - tr
                steps += 1
                if northwestR in range (0,len(matrix)) and  northwestC in range (0,len(matrix)):
                    successors.append(([northwestR,northwestC,flip], steps)) 
          
#-------------------------------------------------------------------------------------------------
        
    if flip == False:
        # if the children of this search need to be flipped, this will be the information that is given to the next nodes
        flip = True
        if (matrix[cr][cc] == 'N'):
            for tr in range(1,len(matrix)):
                north = cr - tr
                steps += 1 
                if north in range (0,len(matrix)):
                    successors.append(([north,cc,flip],steps))

        if (matrix[cr][cc] == 'S'):
            for tr in range(1,len(matrix)):
                south = cr + tr
                steps += 1
                if south in range (0,len(matrix)):
                    successors.append(([south,cc,flip],steps)) 

        if (matrix[cr][cc] == 'E'):
            for tc in range(1,len(matrix)):
                east = cc+tc
                steps += 1
                if east in range (0,len(matrix)):
                    successors.append(([cr,east,flip], steps))

        if (matrix[cr][cc] == 'W'):
            for tc in range(1,len(matrix)):
                west = (cc-tc)
                steps += 1
                if west in range (0,len(matrix)):
                    successors.append(([cr,west,flip],steps))

        if (matrix[cr][cc] == 'NE'):
            for tr in range(1,len(matrix)):
                northeastR = cr - tr
                northeastC = cc + tr
                steps += 1
                if northeastR in range (0,len(matrix)) and northeastC in range (0,len(matrix)):
                    successors.append(([northeastR,northeastC,flip],steps)) 

        if (matrix[cr][cc] == 'NW'):
            for tr in range(1,len(matrix)):
                northwestR = cr - tr
                northwestC = cc - tr
                steps += 1
                if northwestR in range (0,len(matrix)) and  northwestC in range (0,len(matrix)):
                    successors.append(([northwestR,northwestC,flip], steps)) 

        if (matrix[cr][cc] == 'SE'):
            for tr in range(1,len(matrix)):
                southeastR = cr + tr
                southeastC = cc + tr
                steps += 1
                if southeastR in range (0,len(matrix)) and southeastC in range (0,len(matrix)):
                    successors.append(([southeastR,southeastC,flip],steps))


        if (matrix[cr][cc] == 'SW'):
            for tr in range(1,len(matrix)):
                southwestR = cr + tr
                southwestC = cc - tr
                steps += 1
                if southwestR in range (0,len(matrix)) and southwestC in range (0,len(matrix)):
                    successors.append(([southwestR,southwestC,flip],steps))
    return successors

def create():
    #input matrix size 
    size = int(input("enter the size of square matrix: \n"))
    maze = []
    print("please enter the maze in a row wise pattern")
    for i in range (size):
        elements = list(map(str, input().split()))
        maze.append(elements) 
    return maze
def dfs(cr,cc,maze):
    flip = False
    start = ([cr,cc,flip])
    visited = []
    stack = [(start,[start],0)]
    while stack:
        curr, path, cost = stack.pop()
        print(curr,path)
        print("len of path: ",len(path))
        if curr in visited:
            continue
        visited.append(curr)
        if (maze[curr[0]][curr[1]] == 'F'):
            return path,(len(path)-1)
        if (len(path) == 1):
            for next_pos, next_steps in successor(curr[0],curr[1],maze,flip):
                stack.append((next_pos, path+[next_pos],cost + next_steps))
        elif(len(path) > 1):
            flip = curr[2]
            for next_pos, next_step in successor(curr[0],curr[1],maze,flip):
                stack.append((next_pos, path+[next_pos],cost + next_step))
           # for next_pos, next_steps in successor(curr[0],curr[1],maze,flip):
           #     print("hi",next_pos,next_pos)
    return [],10 



#def dfs(cr,cc,maze):
#    flip = False
#    start = ([cr,cc,flip])
#    visited = []
#    stack  = [(start,[start], 0 )]
#    while stack:
#        curr , path , cost = stack.pop()
#        # print(curr)
#        if (curr) in visited:
#            continue
#        visited.append(curr)
#        print(curr[0], curr[1])
#        if (maze[curr[0]][curr[1]]) == 'F':
#            return path, (len(path)-1)
#        if len(path) == 1:
#            for next_pos, next_steps in successor(curr[0],curr[1],maze,curr[2]):
#                stack.append((next_pos, path + [next_pos], cost + next_steps))
#        elif len(path) > 1:
#            parentloc = (len(path)-1)
#            if (path[parentloc][2]) == False:
#                flip = True
#                for next_pos, next_steps in successor(curr[0],curr[1],maze,flip):
#                    stack.append((next_pos, path + [next_pos], cost + next_steps))
#    return [],(len(path)-1)

def bfs(cr,cc,maze):
    start2 = ([cr,cc])
    visited2 = []
    queue = [[start2,[start2],0]]
    while queue:
        current,path2,cost2 = queue.pop(0)
        if current in visited2:
            continue
        visited2.append(current)
        if (maze[current[0]][current[1]]) == 'F':
            return path2, (len(path2)-1)
        for neighbor,cost2 in successor(current[0],current[1],maze):
            queue.append((neighbor, path2 + [neighbor], cost2))
    return [],(len(path2)-1)

def iterative_deepening(cr,cc,maze,depth,path,visited):
    curr3 = ([cr,cc])
    if depth == 0:
        return None
    if curr3 in visited:
        return None
    visited.append(curr3)
    if (maze[curr3[0]][curr3[1]]) == 'F':
        return path + [curr3]
    for neighbor,cost in successor(curr3[0],curr3[1],maze):
        result = iterative_deepening(neighbor[0],neighbor[1],maze,depth,path+[curr3],visited)
        if result is not None:
            return result
    return None

def solve_iter(cr,cc,maze):
    visited = []
    for depth in range (1, len(maze) * len(maze[0]) + 1):
        result = iterative_deepening(cr ,cc ,maze,depth,[],visited)
        if result is not None:
            return result
    return None
    



#------------------------------main--------------------------------
from collections import defaultdict 
maze = create()
dfs_path, dfs_cost = dfs(0,0,maze)
if len(dfs_path) != 0:
    print("dfs path : ",dfs_path)
    print("dfs cost : ",dfs_cost)
else: 
    print("no dfs solution")

print("--------------------------------------- \n ")

#bfs_path, bfs_cost = bfs(0,0,maze)
#if len(bfs_path) != 0:
#    print("bfs path : ",bfs_path)
#    print("bfs cost : ",bfs_cost)
#else:
#    print("no bfs solution")



print("--------------------------------------- \n ")

#idl_path = solve_iter(0,0,maze)
#if len(idl_path) != 0:
#    print("iterative deepening learning path : ",idl_path)
#    print("iterative deepening learning cost : ",(len(idl_path)-1))
#else:
#    print("no iterative deepening solution")
