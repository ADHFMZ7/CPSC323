#ifndef PARSER_H
#define PARSER_H

#include "macros.h"
#include "lexer.h"

typedef enum node_type 
{

	PROG, EXPR, DECLIST, STATLIST,

	DEC, STAT, TYPE

	

	// VOID	

} node_type;

typedef struct AST_Node
{
	node_type type; //
	byte *lexeme;    // 
	u8 line;		     // line of lexeme in source code. used for error handling

} AST_Node;

// This struct handles the internal state of the scanner
typedef struct Parser
{	
	Token *tokens;
	usize current;
} Parser;

AST_Node *parse_tokens(Token *tokens);

#endif
