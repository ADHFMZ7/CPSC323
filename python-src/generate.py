from error import report_gen_error

# PROGRAM <prog_name> ; var <dec-list> begin <stat-list> end.

class AST_Node:
    pass    

# FIX THE AFTER FINAL TOKEN BUG

def generate_code(tokens, out_file, all_errors=0):
    curr = 0 
    token = tokens[curr]
   
    ret = 1

    with open(out_file, "w") as file:
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
                    a = tokens[curr+2].lexeme.strip('",') + ' '
                    num = tokens[curr+3]
                    curr += 5
                else:
                    a = ''
                    num = tokens[curr+2]
                    curr += 4

                if num.lexeme not in var_names:
                    report_gen_error(f"Use of undeclared identifier <{num.lexeme}>", num)
                    if not all_errors:
                        return False 
                    ret = 0 

                print(f'printf("{a}%d\\n", {num.lexeme});', file=file)
            elif token.type == ';':
                print(";", file=file)
            else:
                if token.type == "IDENTIFIER" and token.lexeme not in var_names:
                    report_gen_error(f"Use of undeclared identifier <{token.lexeme}>", token)
                    if not all_errors:
                        return False
                    ret = 0
                print(token.lexeme, end='', file=file)
            curr += 1
            token = tokens[curr]

    return ret 

