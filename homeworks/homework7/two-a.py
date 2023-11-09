"""
Group names: Ahmad Aldasouqi, Kevin Kiely, Ahmir 
Assignment : No. 7
Due Date   : 10/31/23
"""

import sys

def main():

    if len(sys.argv) <= 1:
        print(f"Usage: python3 {sys.argv[0]} [expression]")
        return False
     
    input_string = sys.argv[1].replace(' ', '')

    table = {
            'E': {'i': 'TQ', '+': ''   , '-': ''   , '*': ''   , '/': ''   , '(': 'TQ' , ')': '' , '$':  ''},
            'Q': {'i': ''  , '+': '+TQ', '-': '-TQ', '*': ''   , '/': ''   , '(': ''   , ')': '_', '$': '_'},
            'T': {'i': 'FR', '+': ''   , '-': ''   , '*': ''   , '/': ''   , '(': 'FR' , ')': '' , '$':  ''},
            'R': {'i': ''  , '+': '_'  , '-': '_'  , '*': '*FR', '/': '/FR', '(': ''   , ')': '_', '$': '_'},
            'F': {'i': 'i' , '+': ''   , '-': ''   , '*': ''   , '/': ''   , '(': '(E)', ')': '' , '$':  ''},
            }

    stack = ['$', 'E']

    curr_char = 0

    while stack:
        state = stack.pop()

        if state == input_string[curr_char]: 
            print(stack)
            curr_char += 1

        elif state in table.keys() and input_string[curr_char] in table[state]:
            try:
                entry = reversed(table[state][input_string[curr_char]])
            except KeyError:
                print("Invalid symbol:", curr_char)
                return False

            for s in entry:
                if s == '':
                    print("Input rejected")
                    return False
                elif s == '_':
                    continue
                stack.append(s)

        else:
            print("Input rejected")
            return False

    print("Input accepted")
    return True

if __name__ == "__main__":
    main()
