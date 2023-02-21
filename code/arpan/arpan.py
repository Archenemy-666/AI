def dfs(cr,cc,maze):
    flip = False
    start = ([cr,cc,flip])
    visited = []
    stack = [(start,[start],0)]
    while stack:
        curr, path, cost = stack.pop()
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

def bfs(cr,cc,maze):
    flip = False
    start2 = ([cr,cc,flip])
    visited2 = []
    queue = [[start2,[start2],0]]
    while queue:
        current,path2,cost2 = queue.pop(0)
        if current in visited2:
            continue
        visited2.append(current)
        if (maze[current[0]][current[1]]) == 'F':
            return path2, (len(path2)-1)
        if (len(path2) == 1):
            for neighbor,cost2 in successor(current[0],current[1],maze,flip):
                queue.append((neighbor, path2 + [neighbor], cost2))
        elif(len(path2) > 1):
            flip = current[2]
            for neighbor,cost2 in successor(current[0],current[1],maze,flip):
                queue.append((neighbor, path2 + [neighbor],cost2))
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
            return result, (len(result)-1)
    return None,0