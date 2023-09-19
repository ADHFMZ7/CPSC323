import sys



def main():

    if len(sys.argv) < 2:
        print("Please run command with input argument")
        exit(1)

    inp = sys.argv[1] 
    
    
    fa = {
        0: {'a': 0, 'b': 1, 'c': 2},
        1: {'a': 2, 'b': 1, 'c': 4},
        2: {'a': 1, 'b': 4, 'c': 4},
        'finish': (1, 2)
    }

    print(str(validate(inp, fa)))

def validate(input_string, fa):

    state = 0

    for symbol in input_string:
        print(symbol, state)
        state = fa[state][symbol] 
        if state == 4:
            return False

    return state in fa['finish']

if __name__ == '__main__':
    main()
