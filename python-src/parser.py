"""
Group names: Ahmad Aldasouqi, Kevin Kiely, Ahmir 
Assignment : No. 7
Due Date   : 10/31/23
"""

import sys
from table import table, lookup
from tokenizer import tokenize_source, Token
from error import report_parse_error

def parse_expressions(tokens, all_errors=0):


    stack = ['$', 'A']

    curr_char = 0

    result = 1

    while stack:
        state = stack.pop()
        if tokens[curr_char].type == "STRING":
            current_token = "STRING"
        elif tokens[curr_char].type == "IDENTIFIER":
            current_token = "B"
        elif tokens[curr_char].type == "int":
            current_token = "S"
        else:
            current_token = tokens[curr_char].type

        if state == current_token: 
            if current_token == "B":
                # print(tokens[curr_char].lexeme, end=" ")
                pass
            elif current_token == "S": #int
                # print(tokens[curr_char].lexeme, end=" ")
                pass
            elif current_token == "STRING":
                # print(tokens[curr_char].lexeme + ',', end=" ")
                pass
            else:
                # print(current_token, end=" ")
                pass
            curr_char += 1

        elif state in table.keys() and current_token in table[state]:

            if lookup(state, current_token):
                entry = table[state][current_token].split()[::-1]
            else:
                report_parse_error("Illegal transition", tokens[curr_char], state)
                result = -1
                if all_errors:
                    continue
                return False

            for s in entry:
                if s == '_' or s == ' ':
                    continue
                stack.append(s)

        else:
            report_parse_error("Unexpected token", tokens[curr_char], state)
            result = -1
            if all_errors:
                continue
            return False

    return result

