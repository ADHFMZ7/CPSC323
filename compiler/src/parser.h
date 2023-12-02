#include "macros.h"

typedef enum node_type 
{

	COMMA, COLON, SEMICOLON, 
	EQUALS, PLUS, MINUS, DIV, MUL,

	LEFT_PAREN, RIGHT_PAREN,

	NUMBER, IDENTIFIER, STRING,

	// keywords
	PROGRAM, VAR, BEGIN, END, INTEGER, WRITE,

	VOID	
	

} node_type;

typedef struct AST_Node
{
	node_type type; //
	byte *lexeme;    // 
	u8 line;		     // line of lexeme in source code. used for error handling

} Token;

// This struct handles the internal state of the scanner
typedef struct Parser
{	
	byte *source;
	Token *tokens;
	usize tok_count;

	usize start;
	usize current;
	usize line;

} Scanner;
