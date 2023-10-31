import sys

def main():

    if len(sys.argv) <= 1:
        print(f"Usage: python3 {sys.argv[0]} [expression]")
        return False
     
    input_string = sys.argv[1]

    table = {
            'E': {'i': 'TQ', '+': ''   , '-': ''   , '*': ''   , '/': ''   , '(': 'TQ' , ')': '' , '$':  ''},
            'Q': {'i': ''  , '+': '+TQ', '-': '-TQ', '*': ''   , '/': ''   , '(': ''   , ')': '_', '$': '_'},
            'T': {'i': 'FR', '+': ''   , '-': ''   , '*': ''   , '/': ''   , '(': 'FR' , ')': '' , '$':  ''},
            'R': {'i': ''  , '+': '_'  , '-': '_'  , '*': '*FR', '/': '/FR', '(': ''   , ')': '_', '$': '_'},
            'F': {'i': 'i' , '+': ''   , '-': ''   , '*': ''   , '/': ''   , '(': '(E)', ')': '' , '$':  ''},
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
                print("Invalid symbol:", curr_char)
                return False

            for s in entry:
                if s == '_':
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
