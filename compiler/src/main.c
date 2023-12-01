#include "lexer.h"
#include <stdlib.h>
#include <stdio.h>


i32 main(i32 argc, byte **argv)
{
	
	FILE *file = fopen("finalv1.txt", "rb");
	if (file == NULL) {
		perror("fopen");
		exit(EXIT_FAILURE);
	}

	fseek(file, 0, SEEK_END);
	i64 file_size = ftell(file);
	rewind(file);

	byte *buffer = (char *)malloc(file_size + 1);
	fread(buffer, 1, file_size, file);
	buffer[file_size] = '\0';
	
	fclose(file);
	
	Token *tokens = tokenize_source(buffer);

	// MAKE IT APPEND A VOID TOKEN AFTER TO DENOTE END OF LIST

	free(buffer);
}
