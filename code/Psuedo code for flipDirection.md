The below is the Pseudo code for solving the Spanish Rice Maze problem which takes in square matrix as input and start node is by default considered as the first the 0th row and 0th column of the maze.

```python 
function successor (currentRow, currentColumn, maze, path):
	successors = [] 
	steps = 0
	if matrix[currentRow][currentColumn] is 'N':
		if False in path[0]:
			use condition for 'S'
			append successorsList,cost,if_Switched(True) to successors
			
	if matrix[currentRow][currentColumn] is 'S':	
		if False in path[0]:
			use condition for 'N'
			append successorsList,cost,if_Switched(True) to successors
	
	if matrix[currentRow][currentColumn] is 'E':	
		if False in path[0]:
			use condition for 'W'
			append successorsList,cost,if_Switched(True) to successors

	if matrix[currentRow][currentColumn] is 'W':	
		if False in path[0]:
			use condition for 'E'
			append successorsList,cost,if_Switched(True) to successors

	if matrix[currentRow][currentColumn] is 'NE':	
		if False in path[0]:
			use condition for 'SW'
			append successorsList,cost,if_Switched(True) to successors

	if matrix[currentRow][currentColumn] is 'NW':	
		if False in path[0]:
			use condition for 'SE'
			append successorsList,cost,if_Switched(True) to successors

	if matrix[currentRow][currentColumn] is 'SE':	
		if False in path[0]:
			use condition for 'NW'
			append successorsList,cost,if_Switched(True) to successors

	if matrix[currentRow][currentColumn] is 'SW':	
		if False in path[0]:
			use condition for 'NE'
			append successorsList,cost,if_Switched(True) to successors



	if matrix[currentRow][currentColumn] is 'N':
		for temperaryRow in range 0 to length of maze:
			north = columnRow - temperoryRow
			if north is within the size of maze : 
				append [north,currentColumn],if_switched:False to successors
	
	if matrix[currentRow][currentColumn] is 'S':
		for temperoryRow with in the range 0 to size of matrix:
			south = currentRow + temperoryRow
			if south with in the boundries of matrix:
				append [south,currentColumn],if_switched:False to successors
	
	if matrix[currentRow][currentColumn] is 'E':
		for temperoryColumn within the range 0 to size of matrix:
			east = currentColumn + temperoryColumn
			if east is within the matrix:
				append [currentRow,east],if_switched:False to successors

	if matrix[currentRow][currentColumn] is 'W':
		for temperoryColumn within the range 0 to size of matrix:
			west = currentColumn - temperoryColumn
			if west is within the matrix:
				append [currentRow,west],if_switched:False to successors

	if matrix[currentRow][currentColumn] is 'NE':
		for temperory with in the range 0 to size of matrix:
			northEastRow = currentRow - temperory
			northEastColumn = currentColumn + temperory
			if northEastRow and northEastColumn are within the matrix:
				append [northEastRow,northEastColumn],if_switched:False to sucessors

	if matrix[currentRow][currentColumn] is 'NW':
		for temperory with in the range 0 to size of matrix:
			northWestRow = currentRow - temperory
			northWestColumn = currentColumn - temperory
			if northWestRow and northWestColumn are within the matrix:
				append [northWestRow,northWestColumn],if_switched:False to sucessors

	if matrix[currentRow][currentColumn] is 'SE':
		for temperory with in the range 0 to size of matrix:
			southEastRow = currentRow + temperory
			southEastColumn = currentColumn + temperory
			if northEastRow and northEastColumn are within the matrix:
				append [southEastRow,southEastColumn],if_switched:False to sucessors

	if matrix[currentRow][currentColumn] is 'NE':
		for temperory with in the range 0 to size of matrix:
			northWestRow = currentRow - temperory
			northWestColumn = currentColumn - temperory
			if northWestRow and northWestColumn are within the matrix:
				append [northWestRow,northWestColumn],if_switched:False to sucessors

	return the successors, if_switched


function create():
	input size
	maze = []
	print("please enter the maze in a row wise pattern")
		for i within size:
			map the string elements to list
			append the elements to maze list 
		return maze


function depthFirstSearch(currentRow, currentColumn, maze):
	start = ([currentRow,currentColumn])
	visited = []
	stack = [[start, [path of start], 0 as cost]]
	if_switched = False
	while stack is not empty:
		current , path , cost = element poped out of stack
		if currnet is visited:
			continue
		if current is 'F'
			return path, cost
		for next_position , next_steps,if_switched taken from the output of successor function(current,maze) 
			append next_postion, path and cost to the stack 
		return null and cost

function bredth_first_search(currentRow,currentColumn,maze):
	start = ([currentRow,currentColumn])
	visited = []
	queue = [[start,[path of start],0 as cost]]
	if_switched = False
	while elements in queue:
		current, path, cost = element poped out of queue
		if current is visited:
			continue
		if current is 'F':
			return path, cost
		for neighbor, cost,if_switched from successor function(current,maze):
			append neighbor , path cost to the queue
	return null and cost

function iterativeDeepeningLearning(currentRow,currentColumn,depth,path,visited):
	current = ([currentRow,currentColumn])
	if depth is 0:
		return None
	if current is visited:
		return None
	add current to visited
	if current is 'F':
		return path + current
	for neighbor , cost_generated, if_switched from successor function(current,maze):
		result is iterativeDeepeningLearning of (neighbor,maze,depth,path,visited)
		if result is not empty:
			return result
function toprovideDepth(currentRow,currentRow,maze):
	visited = []
	for depth within the (square of matrix size + 1):
		result is function iterativeDeepeningLearning(currentRow,currentColumn,maze,depth,empty path, visited)
		if result is not empty:
			return result
	return None


import Collections for Queue
create maze using create function
print DepthFisrstSearch Path and cost from function depthFirstSearch(0,0,maze), if length of path is not 0
print BreadthFisrstSearch Path and cost from function BreadthFirstSearch(0,0,maze), if length of path is not 0
print IterativeDeepeningLearning Path and cost from function toProvideDepth(0,0,maze), if length of path is not 0

```