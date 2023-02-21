cd /Users/siddarth_chatla/Library/Mobile\ Documents/iCloud\~md\~obsidian/Documents/Spring\ Courses/AI/

Always 
: set list 
to see tab spaces

E S SW
E NW S
N E F


E W S S S
NW SW E E E 
W S W N N 
F S N SW SW
S SW E N S

Working on the code 


# Spanish Rice Problem:
The input for the spanish rice problem:

prompt: enter the size of square matrix:
6
prompt: please enter the maze in a row wise pattern:

E S W SW NW W
SE NE NE E W NE
W N S NE N W
SE SW N N NW E
E SW W SE NW E
N S N W NE F


## Test case:
prompt: enter the size of square matrix:
3
prompt: please enter the maze in a row wise pattern:

E S NE
N S S
F SW S


## No Solution case
prompt: enter the size of square matrix:
3
prompt: please enter the maze in a row wise pattern:

W S NW
N S S
F SW S


	## No solution Code


N -> (i-n, j)
S -> (i+n, j)
E -> (i , j+n)
W -> (i , j-n)
NE -> (i-n,j+n)
NW -> (i-n,j-n)
SE -> (i+n,j+n)
SW -> (i+n,j-n)

``` Python 
n = 3 # size of matrix
visited = []

current = matrix[currentx][currenty] # in this case let us consider i = 1 , j = 1
visited.append(current)
if current == 'F':
	return visited
if (matrix[x][y] == 'N'):
	for i in range(1,n): # n is not included 
		for j in range(1,n):
			# ( now lets consider first set of loop generated to be 1,1) 
			tempi = i-n # tempi is 0 
			tempj = j   # tempj is 1
				if (tempi >= 3 || tempi < 0) && (tempj >= 3 || tempj < 0):
					 current = matrix[x-tempi][y] # in this will be stored the matrix value i.e in maze it will be direction
					 currentx = x-tempi
					 currenty = y
					 return DFS(currentx,currenty,visited)
						
			

```
# chat gpt code 
``` python 

def get_successors(maze, curr):
    i, j = curr
    successors = []
    if maze[i][j] == 'U':
        if i > 0:
            successors.append((i-1, j))
    elif maze[i][j] == 'D':
        if i < len(maze)-1:
            successors.append((i+1, j))
    elif maze[i][j] == 'L':
        if j > 0:
            successors.append((i, j-1))
    elif maze[i][j] == 'R':
        if j < len(maze[0])-1:
            successors.append((i, j+1))
    return successors

def solve_arrow_maze(maze, start):
    stack = [(start, [start])]
    visited = set()
    while stack:
        curr, path = stack.pop()
        if curr in visited:
            continue
        visited.add(curr)
        if maze[curr[0]][curr[1]] == 'E':
            return path
        for next_pos in get_successors(maze, curr):
            stack.append((next_pos, path + [next_pos]))
    return []

# example usage
maze = [
    ['R', 'R', 'R', 'U'],
    ['L', 'L', 'U', 'L'],
    ['L', 'R', 'R', 'R'],
    ['U', 'L', 'L', 'E']
]
start = (0, 0)
print(solve_arrow_maze(maze, start))  # [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3)]



solve arrow maze using dfs
use successor function to list possible steps
generate the path
the arrow maze can take more than one step



pseudo - make changes 
function get_successors(maze, curr):
    i, j = curr
    successors = []
    steps = 0
    if maze[i][j] == 'U':
        while i > 0 and maze[i-1][j] != 'U' and maze[i-1][j] != 'D':
            i -= 1
            steps += 1
        if i > 0:
            append (i-1, j, steps) to successors
    elif maze[i][j] == 'D':
        while i < len(maze)-1 and maze[i+1][j] != 'U' and maze[i+1][j] != 'D':
            i += 1
            steps += 1
        if i < len(maze)-1:
            append (i+1, j, steps) to successors
    elif maze[i][j] == 'L':
        while j > 0 and maze[i][j-1] != 'L' and maze[i][j-1] != 'R':
            j -= 1
            steps += 1
        if j > 0:
            append (i, j-1, steps) to successors
    elif maze[i][j] == 'R':
        while j < len(maze[0])-1 and maze[i][j+1] != 'L' and maze[i][j+1] != 'R':
            j += 1
            steps += 1
        if j < len(maze[0])-1:
            append (i, j+1, steps) to successors
    return successors

function solve_arrow_maze(maze, start):
    stack = [(start, [start], 0)]
    visited = set()
    while stack is not empty:
        curr, path, cost = pop from stack
        if curr is in visited:
            continue
        add curr to visited
        if maze[curr[0]][curr[1]] == 'E':
            return path, cost
        for next_pos, next_steps in get_successors(maze, curr):
            append (next_pos, path + [next_pos], cost + next_steps) to stack
    return [], 0


10 def bfs(cr,cc,maze):
111     start = ([cr,cc])
112     queue = collections.deque([(start, [start], 0)])
113     visited = set()
114     while queue:
115         curr, path, cost = queue.popleft()
116         if curr in visited:
117             continue
118         visited.add(curr)
119         if maze[curr[0]][curr[1]] == 'E':
120             return path,cost
121










import collections

def get_successors(maze, curr):
    i, j = curr
    successors = []
    if maze[i][j] == 'U':
        while i > 0 and maze[i-1][j] != 'U' and maze[i-1][j] != 'D':
            i -= 1
        if i > 0:
            successors.append((i-1, j))
    elif maze[i][j] == 'D':
        while i < len(maze)-1 and maze[i+1][j] != 'U' and maze[i+1][j] != 'D':
            i += 1
        if i < len(maze)-1:
            successors.append((i+1, j))
    elif maze[i][j] == 'L':
        while j > 0 and maze[i][j-1] != 'L' and maze[i][j-1] != 'R':
            j -= 1
        if j > 0:
            successors.append((i, j-1))
    elif maze[i][j] == 'R':
        while j < len(maze[0])-1 and maze[i][j+1] != 'L' and maze[i][j+1] != 'R':
            j += 1
        if j < len(maze[0])-1:
            successors.append((i, j+1))
    return successors

def dfs_with_depth_limit(maze, curr, end, path, visited, depth_limit):
    if depth_limit == 0:
        return None
    if curr in visited:
        return None
    visited.add(curr)
    if curr == end:
        return path + [end]
    for neighbor in get_successors(maze, curr):
        result = dfs_with_depth_limit(maze, neighbor, end, path + [curr], visited, depth_limit-1)
        if result is not None:
            return result
    return None

def solve_arrow_maze(maze, start, end):
    for depth_limit in range(1, len(maze) * len(maze[0]) + 1):
        result = dfs_with_depth_limit(maze, start, end, [], set(), depth_limit)
        if result is not None:
            return result
    return None

maze = [['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
        ['U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'R'],
        ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'U', 'R'],
        ['R', 'R', 'R', 'R', 'R', 'R', 'L', 'U', 'R'],


