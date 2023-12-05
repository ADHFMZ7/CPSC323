"""
Group names: Ahmad Aldasouqi, Kevin Kiely, Ahmir 
Assignment : No. 7
Due Date   : 10/31/23
"""

import sys
from table import table, lookup
from tokenizer import tokenize_source, Token

def main():

    if len(sys.argv) <= 1:
        print(f"Usage: python3 {sys.argv[0]} [expression]")
        return False

    with open(sys.argv[1]) as file_text:
        input_string = file_text.read()

    tokens = tokenize_source(input_string)
   
    stack = ['$', 'A']

    curr_char = 0

    while stack:
        print("Stack: ", stack)
        state = stack.pop()

        if state == tokens[curr_char]: 
            print(stack)
            curr_char += 1

        elif state in table.keys() and tokens[curr_char] in table[state]:

            if lookup(state, tokens[curr_char]):
                entry = reversed(table[state][tokens[curr_char]])
            else:
                print("Input rejected")
                return False

            for s in entry:
                if s == '_' or s == ' ':
                    continue
                stack.append(s)

        else:
            print("Input rejected")
            return False

    print("Input accepted")
    return True

if __name__ == "__main__":
    main()
