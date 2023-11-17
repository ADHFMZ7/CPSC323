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
	usize start;
	usize current;
	usize line;

} Scanner;

Token *tokenize_source(byte *source);


#endif
