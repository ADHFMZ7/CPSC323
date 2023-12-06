# Design Doc

This compiler implements the toy langauge given in class.

The compiler is written in python and it compiles down to C.

It has the following structure:
Source -> [Lexer] -> Tokens -> [LL Parser] -> C code.

## Lexer
The compiler uses a simple lexer that runs in O(n) time.

## LL Parser
This project uses a LL(Left to right, Leftmost derivation) technique to parse the syntactic grammar of the language.

## Code generation
The compiler uses a very rudimentary technique to generate code. It checks for very simple semantic errors and 
the equivalent C code.

