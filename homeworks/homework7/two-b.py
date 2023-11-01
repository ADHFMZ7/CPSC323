"""
Group names: Ahmad Aldasouqi, Kevin Kiely, Ahmir 
Assignment : No. 7
Due Date   : 10/31/23
"""

import sys

def main():

    if len(sys.argv) <= 1:
        print(f"Usage: python3 {sys.argv[0]} [filename]")
     
    input_string = sys.argv[1]

    table = {
            'S': {'a': 'aW', '+': ''   , '-': ''   , '*': ''   , '/': ''   , '(': 'aW' , ')': ''  , '$':  '' , '=': ''  },
            'W': {'a': '=E', '+': ''   , '-': ''   , '*': ''   , '/': ''   , '(': '=E' , ')': '_' , '$': '_' , '=': '=E'},
            'E': {'a': 'TY', '+': ''   , '-': ''   , '*': ''   , '/': ''   , '(': 'TY' , ')': ''  , '$':  '' , '=': ''  },
            'Y': {'a': ''  , '+': '+TY', '-': '-TY', '*': 'R'  , '/': ''   , '(': ''   , ')': '_' , '$': '_' , '=': ''  },
            'T': {'a': 'FP', '+': ''   , '-': ''   , '*': ''   , '/': ''   , '(': 'FP' , ')': ''  , '$':  '' , '=': ''  },
            'P': {'a': ''  , '+': '_'  , '-': '_'  , '*': '*FP', '/': '/FP', '(': ''   , ')': '_' , '$':  '_', '=': ''  },
            'F': {'a': 'a' , '+': ''   , '-': ''   , '*': ''   , '/': ''   , '(': '(E)', ')': ''  , '$':  '' , '=': ''  },
            }

    stack = ['$', 'S']

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
