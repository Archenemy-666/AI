
# AIMA Problem solving 
``` python
function SIMPLE-PROBLEM-SOLVING-AGENT(percept) returns an action 
	static: seq, an action sequence, initially empty
			state, some description of the current world state
			goal, a goal, initially null 
			problem, a problem formulation
	state <-- UPDATE-STATE(state, percept)
	if seq is empty then do
		goal <-- FORMULATE-GOAL(state)
		problem <-- FORMULATE-PROBLEM(state, goal)
		seq <-- SEARCH(problem)
	action <-- FIRST(seq)
	seq <-- REST(seq)
	return action
	
```

__What is the branching factor.__

# Questions
- can the maze problem be a factored representation ?
- can an uninformed search push the agent to always be in a transistion loop? 
- can a sensorless be truely a solution.--> we cannot have a non deterministic & sensorless

