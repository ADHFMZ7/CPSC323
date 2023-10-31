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
            'T': {'a': 'FY', '+': ''   , '-': ''   , '*': ''   , '/': ''   , '(': ''   , ')': 'FY', '$':  '' , '=': ''  },
            'P': {'a': ''  , '+': '_'  , '-': '_'  , '*': '*FP', '/': '/FP', '(': ''   , ')': '_' , '$':  '_', '=': ''  },
            'F': {'a': 'a' , '+': ''   , '-': ''   , '*': ''   , '/': ''   , '(': '(E)', ')': ''  , '$':  '' , '=': ''  },
            }

    stack = []
    stack.append('$')
    stack.append('E')

    curr_char = 0

    while stack:

        #print(stack)       
        state = stack.pop()

        if state in table.keys():
            try:
                entry = reversed(table[state][input_string[curr_char]])
            except KeyError:
                print("Invalid symbol:", input_string[curr_char])
                return False

            for s in entry:
                if s == '':
                    print("Input rejected")
                    return False
                stack.append(s)
        elif state in table['E'].keys(): 
            print(stack)
            curr_char += 1
        else:
            print("Invalid key")

    print("Input accepted")
    return True

if __name__ == "__main__":
    main()
