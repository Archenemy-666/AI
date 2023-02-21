Informed : using a (hand-crafted) heuristic to capture past experience or intuition.


# Constraints on best first heuristics
We will formalize a heuristic h(n) as follows:  
h(n) ≥ 0 for all nodes n  
h(n) = 0 implies that n is a goal node  
h(n) = ∞ implies that n is a “dead end” from  
which a goal cannot be reached
- pruning a search based on h(n)

# Best first Search:
Best-first search uses an evaluation function f(n), incorporating some heuristic component, h(n) and sometimes the cost of getting to a node, g(n
- f(n) is used to sort an open list, ie using a priority queue (like UCS)

## Greedy Best first search
- Greedy search (GS) uses a simple evaluation function of  
f(n) = h(n), ie f(n) = 1*h(n) + 0*g(n).
- It ignores the cost of getting to a state, and picks based only on h


Greedy example: 
f(n) = h(n) ==> in slide 8 

Greedy Search pro and cons 
pro : generally faster than uninformed, because it could have more knowledge about the problem domain. __If the h(n) is good__

con : neither comeplete (might follow an infinite path) nor optimal (without considering alternative paths)


## A search
f(n) = 1*g(n) + 1*h(n)
The value g(n) is the minimal cost path from the initial node to the current node (which might need to be updated during a search).

f(n) = g(n) + h(n) ==> slide 22 



-----------------sub optimal searching next class ----------------------------------
