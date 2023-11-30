#include "macros.h"
#include "lexer.h"
#include <string.h>
#include <stdio.h>
#include <wctype.h>

#define BUF_SIZE 1024

byte *substr(byte *source, usize start, usize current)
{

	i32 len = current - start;
	byte *buffer = (byte *) malloc(sizeof(byte) * len);

	for (usize ix = 0; ix < len; ix++)
	{
		buffer[ix] = source[start + ix];
	}

	return buffer;
}

void add_token(Scanner *scanner, token_type type)
{

	// Cover case where the token array exceeds the buffer count.

	scanner->tokens[scanner->tok_count].type = type;
	scanner->tokens[scanner->tok_count].lexeme = substr(scanner->source, scanner->start, scanner->current);
	scanner->tokens[scanner->tok_count++].line= scanner->line;

	printf("New Token <%s> of type %d\n", scanner->tokens[scanner->tok_count-1].lexeme, scanner->tokens[scanner->tok_count-1].type);
	// printf("New Token of type %d\n", scanner->tokens[scanner->tok_count-1].type);

	scanner->start = scanner->current;
}

byte next_char(Scanner *scanner)
{
	return scanner->source[scanner->current++];
}

byte peek(Scanner *scanner)
{
	return scanner->source[scanner->current];
}

token_type identifier(char *string)
{
	if (strcmp(string, "program"))
	{
		return PROGRAM;
	}
	else if (strcmp(string, "var"))
	{
		return VAR;
	}
	else if (strcmp(string, "begin"))
	{
		return BEGIN;
	}
	else if (strcmp(string, "integer"))
	{
		return INTEGER;
	}
	else if (strcmp(string, "write"))
	{
		return WRITE;
	}
	else if (strcmp(string, "end"))
	{
		return END;
	}
	else
	{
		return VOID;
	}
}

Token *tokenize_source(byte *source)
{

	usize src_len = strlen(source);
	Scanner scanner = {.source = source,
										 .tokens = (Token *) malloc(sizeof(Token) * BUF_SIZE),
										 .tok_count = 0,
										 .start = 0, 
										 .current = 0, 
									   .line= 1 };

	Token *tokens = malloc(sizeof(Token) * BUF_SIZE);

	while (scanner.current < src_len)
	{
		byte c = next_char(&scanner);

		while (iswspace(c)) 
		{
			if (c == '\n') scanner.line++;
			scanner.start = scanner.current;
			c = next_char(&scanner);
		}

		switch (c)
		{
			case '(':
				// Handle condition of it being a comment	
			
	
				// (* the text of the comment *)
				if (peek(&scanner) == '*') 
				{
					// We are in a comment
					next_char(&scanner);
					while (next_char(&scanner) != '*' && peek(&scanner) != ')') {}
					next_char(&scanner);
					scanner.start = scanner.current;
					break;
				}
				else 
				{
					add_token(&scanner, LEFT_PAREN); break;
				}
			
			case ')': add_token(&scanner, RIGHT_PAREN); break;
			case ',': add_token(&scanner, COMMA);       break;
			case ';': add_token(&scanner, SEMICOLON);   break;
			case ':': add_token(&scanner, COLON);       break;
			case '=': add_token(&scanner, EQUALS);	  	break;
			case '+': add_token(&scanner, PLUS);	  		break;
			case '-': add_token(&scanner, MINUS);	  		break;
			case '*': add_token(&scanner, MUL);		  		break;
			case '/': add_token(&scanner, DIV);		  		break;
			case '"':
				next_char(&scanner);
				while (peek(&scanner) != '"')
				{
					next_char(&scanner);
				}
				next_char(&scanner);
				add_token(&scanner, STRING);
				break;

			default:  
				
				token_type identifier_type = identifier(substr(scanner.source, scanner.start, scanner.current));

				if (identifier_type != VOID)
				{
					break;
				}
					printf("UNKNOWN TOKEN %s\n", substr(scanner.source, scanner.start, scanner.current));
					break;
			
			// if (c == )	

			// Now handle number, identifier, keywords, string case


		}

	}
	return tokens;
}
