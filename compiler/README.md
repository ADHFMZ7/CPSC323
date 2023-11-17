# Design Doc

This compiler implements the toy langauge given in class.

It will be written as a C frontend that compiles to the LLVM IR language. This allows us to benefit from the many optimizations offered by the LLVM project as well as being in a portable form.


Source -> [Lexer] -> Tokens -> [LR Parser] -> AST -> [Front End] -> LLVM IR -> [LLVM Backend] -> Optimized binary

## Lexer
The compiler uses a simple lexer that runs in O(n) time.

## LR Parser
This project uses a LR(Left to right, Rightmost derivation) technique to parse the semantic grammar of the language.

## Front End
