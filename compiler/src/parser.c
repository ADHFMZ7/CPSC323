#include "parser.h"
#include "lexer.h"
#include <stdio.h>

typedef struct Stack {
    enum token_type* array;
    int capacity;
    int top;
} Stack;

void initialize_stack(struct Stack* stack, int capacity) {
    stack->array = (enum token_type*)malloc(capacity * sizeof(enum token_type));
    stack->capacity = capacity;
    stack->top = -1; // Initialize top to -1 to indicate an empty stack
}

int is_empty(struct Stack* stack) {
    return (stack->top == -1);
}

int is_full(struct Stack* stack) {
    return (stack->top == stack->capacity - 1);
}

void push(struct Stack* stack, enum token_type data) {
    if (is_full(stack)) {
        fprintf(stderr, "Error: Stack is full\n");
        exit(EXIT_FAILURE);
    }
    stack->array[++stack->top] = data;
    printf("Pushed %d onto the stack\n", data);
}

// Function to pop an element from the stack
enum token_type pop(struct Stack* stack) {
    if (is_empty(stack)) {
        fprintf(stderr, "Error: Stack is empty\n");
        exit(EXIT_FAILURE);
    }
    enum token_type data = stack->array[stack->top--];
    printf("Popped %d from the stack\n", data);
    return data;
}

AST_Node *parse_tokens(Token *tokens)
{

    Parser parser;
    parser.tokens = tokens;
    parser.current = 0;
   
    Stack stack;  
    initialize_stack(&stack, 1024);

    push(&stack, VOID);
    push(&stack, PROGRAM);


    while (!is_empty(&stack))
    {
	

    }

}




