from error import report_gen_error
import os

# PROGRAM <prog_name> ; var <dec-list> begin <stat-list> end.

class AST_Node:
    pass    



def generate_code(tokens):
    curr = 0 
    token = tokens[curr]
    
    with open("main.c", "w") as file:
        # program <identifier>;
        print("#include <stdio.h>\nint main() {", file=file)
        curr += 4
        token = tokens[curr]

    
        var_names = []
        # var <dec-list>
        print("int ", end='', file=file)
        while True:
            if token.type == ":":
                print(';', file=file)
                break
            else:
                if token.lexeme != ',':
                    var_names.append(token.lexeme) 
                print(f"{token.lexeme} ", end='', file=file) 
            curr += 1
            token = tokens[curr]
        curr += 4
        token = tokens[curr]


        # begin <stat-list> end.
        while True:
            if token.type == "end.":
                print("return 0;\n}", file=file)
                break
            elif token.type == "write":
                if tokens[curr + 2].type == "STRING":
                    a = tokens[curr+2].lexeme.strip('",')
                    print(f'printf("{a} %d\\n", {tokens[curr+3].lexeme});', file=file)
                    curr += 5
                else:
                    print(f'printf("%d\\n", {tokens[curr+2].lexeme});', file=file)
                    curr += 4
            elif token.type == ';':
                print(";", file=file)
            else:
                if token.type == "IDENTIFIER" and token.lexeme not in var_names:
                    report_gen_error(f"Use of undeclared identifier <{token.lexeme}>", token)
                    os.remove("main.c")
                print(token.lexeme, end='', file=file)
            curr += 1
            token = tokens[curr]




