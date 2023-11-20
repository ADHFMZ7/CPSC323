#ifndef LEXER_H
#define LEXER_H

#include "macros.h"

typedef enum token_type 
{

	COMMA, COLON, SEMICOLON, 
	EQUALS, PLUS, MINUS, DIV, MUL,

	LEFT_PAREN, RIGHT_PAREN,

	NUMBER, IDENTIFIER, STRING,

	// keywords
	PROGRAM, VAR, BEGIN, END, INTEGER, WRITE

} token_type;

typedef struct Token
{
	token_type type; //
	byte *lexeme;    // 
	u8 line;		     // line of lexeme in source code. used for error handling

} Token;

// This struct handles the internal state of the scanner
typedef struct Scanner
{	
	char *source;
	Token *tokens;
	usize tok_count;

	usize start;
	usize current;
	usize line;

} Scanner;

byte *substr(byte *source, usize start, usize current);

void add_token(Scanner *scanner, token_type type);

byte next_char(Scanner *scanner);

byte peek(Scanner *scanner);

Token *tokenize_source(byte *source);


#endif
