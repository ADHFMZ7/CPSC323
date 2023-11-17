#include "macros.h"
#include "lexer.h"
#include <string.h>
#include <stdio.h>

#define BUF_SIZE 1024

// typedef struct Token
// {
// 	token_type type; //
// 	byte *lexeme;    // 
// 	u8 line;		     // line of lexeme in source code. used for error handling
//
// } Token;
//
// // This struct handles the internal state of the scanner
// typedef struct Scanner
// {	
// 	usize start;
// 	usize current;
// 	usize line;
//
// } Scanner;



Token *tokenize_source(byte *source){

	usize src_len = strlen(source);
	Scanner scanner = {.start=0, .current=0, .line=0}; 

	Token *tokens = malloc(sizeof(Token) * BUF_SIZE);

	while (scanner.current < src_len)
	{
		switch ()
		{
			

		}

	}

}
