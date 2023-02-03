cd /Users/siddarth_chatla/Library/Mobile\ Documents/iCloud\~md\~obsidian/Documents/Spring\ Courses/AI/

Always 
: set list 
to see tab spaces

E S SW
E NW S
N E F

Working on the code 



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
