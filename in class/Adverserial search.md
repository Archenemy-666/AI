# Game Playing in AI :
Game playing for entertainment has a long history –  
playing checkers was the first case of machine learning,  
using __reinforcement learning__ to learn __the heuristic  
function__ for a __Greedy search.__

The most recent game systems use Deep Learning play  
better than “master players” for complex board games  
such as Chess and Go.

# AI for gameplaying:
Game playing or “Adversarial Search” has been thought to  
be a good problem for AI
• __Game playing is non-trivial__  
	• Games can be very complex (e.g. chess, go)  
	• Requires decision making within limited time  
__• Games usually are:__
	• Well-defined and repeatable  
	• Limited and accessible
We can directly compare humans and computers

# Types of Games:
We distinguish games in two ways:
	__Deterministic vs Stochastic__
	__Perfect vs imperfect information__
We will only consider “zero-sum” games in which one player wins  
and the other(s) lose(s).


![[Pasted image 20230213115213.png]]

![[Pasted image 20230213115235.png]]

# Game playing as Search:
considering a two player game
ex: Board Game 
	states : board configuration
	Actions : legal moves
	Initial State : current board configuration. 
	Goal State : winning/terminal board config - but all "wins" are equal. 

# greedy search for a game:
• Expand the search tree to the terminal states  
• Evaluate utility of each terminal board state  
• Make the initial move that results in the board configuration with the maximum value

![[Pasted image 20230213120452.png]]

But this still ignores what the opponent is likely to do...  
• Computer chooses C because its utility is 9  
• Opponent chooses J and wins!

This means that when the oppenant makes the move this means that there is a maximization performed by the opponent and this would become minimization for you. The tables are now flipped.

# MinMax Principle:
We assume the worst (opponent is optimal)
	Low utility numbers favor opponent
	high utility numbers favor computer

The computer assumes after it moves the opponent will choose the minimizing move
Propagating MiniMax Values  
• Explore the tree to the terminal states  
• Evaluate utility of the resulting board configurations  
• The computer makes a move to put the board  
in the best configuration for it, assuming the  
opponent makes its best moves on its turn:  
	• Start at the leaves  
	• Assign value to the parent node as follows  
		• Use minimum when children are opponent’s moves  
		• Use maximum when children are computer's moves


# Staic Board Evaluators (SBE) for depth limited searching:

A static board evaluation function is used to estimate how  
good the current board configuration is for the computer  
- Reflects computer’s chances of winning from that state  
- Must be easy to calculate from board configuration

- Typically, one subtracts how good it is for the  
opponent from how good it is for the computer  
- If the board evaluation has utility x for a player,  
then it is usually considered -x for opponent  
- Must agree with the utility function that is  
calculated at terminal nodes

# Alpha-Beta Pruning:
Some of the branches of the game tree won’t ever be taken  
if playing against an intelligent opponent; so we can “prune”  
those branches
Keep track while doing DFS of game tree of:  
• Maximizing level: alpha  
	• Highest value seen so far  
	• Lower bound on node’s utility or score  
• Minimizing level: beta  
	• Lowest value seen so far  
	• Higher bound on node’s utility or score

When maximizing (computer’s turn):  
• If alpha ≥ parent’s beta, stop expanding  
• Opponent shouldn’t allow the computer to make this  
move

When minimizing (opponent’s turn):
• If beta ≤ parent’s alpha, stop expanding  
• Computer shouldn’t take this route

## Effectiveness of Alpha-Beta:
Effectiveness depends on the order in which successors are examined (more effective if best are examined first)  
	• Best Case:  
		• Each player’s best move is evaluated first (left-most)  
	• Worst Case:  
		• Ordered so that no pruning takes place  
		• No improvement over exhaustive search  
• In practice, performance is closer to the best case than the  
worst case

# Horizon Effect:
- Quiscence Search:
	- When evaluation frequently changing, allow looking deeper than the limit  
	- Looking for a point when game quiets down
- Secondary Search:
	1. Find best move looking to depth d  
	2. Look k steps beyond to verify it still looks good  
	3. If it doesn’t, repeat step 2 for next best move

# Stochastic Game Environments:

playing min-max with the stochastic environment. 
chance is the key word:
![[Pasted image 20230215120507.png]]

take average of the child nodes. In this case is (6+2)/2 = 4. 
The other part is (0 + 4) / 2  = 2 

## Stochastic Game Environments: 
• Stochastic elements increase the branching factor  
	• The value of look-ahead diminishes: as depth increases, probability of reaching a particular node decreases  
	• For example, in backgammon there are more than a million states at depth of 4  
• Alpha-beta pruning is less effective (because pruning works best when searches are deep rather than wide)  
• It is important to have a good evaluation function.

