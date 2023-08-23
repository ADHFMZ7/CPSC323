[TODO: STRUCTURE THESE NOTES BETTER IN THE FUTURE]
# Finite Automata (FA) Notes

defined as a machine with a finite amount of states.

This type of automata is often called a [Finite State Machine](https://en.wikipedia.org/wiki/Finite-state_machine)

A finite state machine is described by an initial state, and can transition to all of the other possible states.

There are some different types of states:

	- Initial State - The initial state is the state the machine is in at the beginning of its life
	- Null State - A null state is a non-final, non-initial state that acts as a transition between two other states.
	- Final State - A final state of the automata is a state that the machine can halt in. (These can be thought of as the outputs??)

FA is described by a set of four symbols:

	[TODO: finish this later based on the handout]

	∑: Set of alphabets = 
	Q: set of possible states
	F: set of final states
	4: 

	There are two ways to describe rules of an FSM

	Transition Table or a Context-Free Grammer (CFG)

	Question: Ask about different notations


## Notations: 
	- (i): the word of length 0 is λ, so |λ| = 0
		if λ is part of a word, you can ignore it.

	- (ii): States
		- Initial state: node with a minus 
		- Final state: node with a plus
		- Null state: empty node
		- Initial and Final state: node with a plus and minus
	
	- (iii):
		A word to a power means we concatonate that word to itself n times
		ex) (ab)^3 = ababab
				a^2b^2 = aabb



	Factoring:
		
	left factoring: a + ab = a(λ + b)
	right factoring: a + ba = (λ + b)a

	a^* = set of all powers of a including the zero pows 
	a^+ = set of all powers of a not including the zero pows

	ex) a^*b^* = {λ, a, b, ab, a^2, b^2, b^3, ab^2, a^3, ...}

	Addition:
		The addition operator of two languages is the union

		ex) a^* + b^* = {λ, a, a^2, ...} + {λ, b, b^2, ...} = {λ, a, b, a^2, b^2, ...}
		
	
