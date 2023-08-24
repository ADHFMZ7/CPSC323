"""

File: main.py


"""

class ENV:
    def __init__(self):
        self.symbols = {}
        self.ops = {
                    '+': lambda a, b: a+b,
                    '-': lambda a, b: b-a,
                    '*': lambda a, b: a*b,
                    '/': lambda a, b: a/b,
                    }

    def __getitem__(self, symbol: str):

        if symbol in self.symbols:
            return self.symbols.get(symbol, None)
        elif symbol in self.ops:
            return self.ops[symbol]

    def __setitem__(self, symbol: str, value: int):
        self.symbols[symbol] = value



def eval_rpn(expression: str, env: ENV):
    """
    Evaluates a string expression in 
    Reverse Polish Notation 
    """
    stack = []

    for i, symbol in enumerate(expression):
        if symbol in env.symbols:
            stack.append(env[symbol])
        elif symbol in env.ops:
            op = env[symbol]
            stack.append(op(stack.pop(), stack.pop()))
    return stack[0] 



def main():

    print("Reverse Polish Notation Calculator")
    print("Type an expression or a command")
    print("Type 'h' for help")

    env = ENV()
    env['a'] = 5
    env['b'] = 7
    env['c'] = 2
    env['d'] = 4
    
    running = 1
    while running:
        text = input(">>> ")
        inp = text.split()
        if len(inp) == 3 and inp[0] == 's':
            try:
                env[inp[1]] = int(inp[2])
            except:
                print("Invalid command")
                continue

        elif inp[0] == 'h':
            print("Commands")
            print("    s: define a variable")
            print("        usage: s [symbol] [value]")
            print("    q: quit the program") 
        elif inp[0] == 'q':
            running = 0
        else:
            value = eval_rpn(text, env)
            if value == None:
                print("invalid command")
                continue
            print(value)
            


if __name__ == "__main__":
    main()

