#include "macros.h"
#include "lexer.h"
#include <string.h>
#include <stdio.h>

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
	scanner->tokens[scanner->tok_count].type = type;
	scanner->tokens[scanner->tok_count].lexeme = substr(scanner->source, scanner->start, scanner->current);
	scanner->tokens[scanner->tok_count++].line= scanner->line;

	printf("New Token %s\n", scanner->tokens[scanner->tok_count-1].lexeme);

	scanner->start = scanner->current;
}

byte next_char(Scanner *scanner)
{
	return scanner->source[scanner->current++];
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
		switch (c)
		{
			case ',': add_token(&scanner, COMMA);     break;
			case ';': add_token(&scanner, SEMICOLON); break;
			case ':': add_token(&scanner, COLON);     break;
			case '=': add_token(&scanner, EQUALS);		break;
			case '+': add_token(&scanner, PLUS);			break;
			case '-': add_token(&scanner, MINUS);			break;
			case '*': add_token(&scanner, MUL);				break;
			case '/': add_token(&scanner, DIV);				break;
			default: break;
		}

	}

}
