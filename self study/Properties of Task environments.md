#AI_NOTES 
## Properties of [[Task environments]] 
The range of task environments is fairly large. We can, however, identify a fairly small number of dimensions along which task environments can be categorized. These dimensions determine, to a large extent, the appropriate __agent design__ and the applicability of each of the principal families of techniques for __agent Implementation__.  

### Dimensions of Task environments.
#### __Fully observable v/s partially observable__ : 
- A task environment is effecetively __fully observable__ if the sensors detect all aspects that are _relevant_ to the choice of action; relavance, in turn, depends on the performance measure. 
- An environment might be __partially observable__ because of noisy and inaccurate sensors or because parts of the state are simply missing from the sensor data.
- __unobservable__ means that there are no sensors for the agents 
- - -

#### __Single Agent v/s multi agent__
- __competitive__ : where one agent tries to increase its performance measure and this reduces the other agents performance. 
- __Partially competitive / Partially cooperative__ : avoids collision (partially cooperative) + cases such as this also includes a competitive communication to avoid collision or gain a better performance measure (ex : taxi driver's).
- __Cooperative__ : where the agents avoid collisions with regard to performance measures. 
- - -

#### __Deterministic v/s stochastic__ : 
__Determinisitc__: If the next state of the environment is completely determined by the current state and the action executed by the agent then we say the environment is determinisitc. 
	___"An agent need not worry about uncertainity in a fully observable, determinisitc environment"___
In definition we ignore uncertainity that arises purely from the actions of other agents in multiagent environments; thus a game can be deterministic even though each agent may not be able to predict the actions of others.

__Stochastic__: If the environment is partially observable then it is called stochastic.
Our use of stochastic generally implies that uncertainity about outcomes is quantified in terms of probabilities. 

__Non Deterministic__ environment is one which actions are charecterized by ___possible___ outcomes, but no probabilities are attached to them. These are usually __associated with performance measures that require__ the ==__agent__ to succeed== for ___all possible___ outcomes of its actions. 
- - - 

#### __Episodic v/s sequential__:
__Episodic environment__, the agent's experience is divided into atomic episodes. In each episode the agent recieved a percept and then performs a single action.

___"Crucially, the next episode does not depend on the action taken in the previous episodes."___
==__Many classification tasks are episodic__==

__Sequential environments:__ The current decisions could affect all future decisions.
ex: chess, taxi, both cases, short term actions can have long term consequences. 
Episodic is simpler than sequential environments because the agents does not have to think ahead.
- - -

#### __Static v/s Dynamic__
__Dynamic__ : IF the environment can change during the agent is deliberating, then we say environment is dynamic.
__Static__ : static environment are easier to deal with because the agent does not have to keep looking at the world while making a decision on an action.

___Dynamic environments keep asking the agents for their action, and when there is no action it is considered as deciding to do nothing.___
==___If the environment itself does not change and the agents performance score changes, then we say that the environment is semidynamic.___==
chess while the game is timed is semidynamic where as taxi driving is dynamic, crossword is static.
- - -

#### __Discrete v/s Continuous__
==__The discrete/continuous distinctions applies to the state of the environment, to the way time is handled and to the percepts and actions of the agents.__==
For chess has a finite number of distinct states and without the clock running has distinct actions and percepts.
Taxi driving is continuous, where state is continuosly evolving and the percepts such as steer is also a continous input. 
- - -

#### __Known v/s Unknown__
The distinction in this case is __not__ to the environment but for the agent's state of knowledge about the "laws of physics" of the environment. 

__known environment__ : In a known environment, the outcome (_outcome probabilities if the environment is stochastic_)for actions are given.

__If the environement is unknown the agent will have to learn how it works to make good decisions.__==Note that the distinction between known and unknown environments is not same as fully and partially observable environments. It is quite possible for a known environment to be partially observable. ==

Ex: solitair card games, I know the rules still unable to see the cards that have not yet been turned over.
Conversely, an _unknown environment_ can be _fully observable_, in a new video gam, the screen may show the entire game state but still dont know what buttons until I try them.
