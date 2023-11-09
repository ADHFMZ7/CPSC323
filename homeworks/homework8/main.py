"""
Group names: Ahmad Aldasouqi, Kevin Kiely, Ahmir 
Assignment : No. 8
Due Date   : 11/07/23
"""

import sys
from table import table, prods

def main():

    if len(sys.argv) <= 1:
        print(f"Usage: python3 {sys.argv[0]} [expression]")
        return False

    input_string = sys.argv[1].replace(' ', '')
    stack = [0]
    curr_char = 0

    while stack:
        print(stack)
        curr_state = int(stack.pop())
        curr_symbol = input_string[curr_char] 

        cell = table[curr_state][curr_symbol]
        if cell == "ACC":
            print("Input Accepted")
            return True

        elif cell == "":
            print("Input Rejected")
            return False

        elif cell.isdigit():
            stack.append(curr_state)
            stack.append(curr_symbol)
            stack.append(int(cell))

        elif cell[0] == 'S':
            new_state = int(cell[1:])
            stack.append(curr_state)
            stack.append(curr_symbol)
            stack.append(new_state)
            print(new_state)
            curr_char += 1

        elif cell[0] == 'R':

            stack.append(curr_state)

            rule = int(cell[1:])
            for _ in range(2 * prods[rule][1]):
                stack.pop()

            new_state = int(stack.pop())
            goto_state = table[new_state][prods[rule][0]]
            stack.append(new_state)
            stack.append(prods[rule][0])
            stack.append(goto_state)


        else:
            print("Input Rejected")
            return False 

    print("Input accepted")
    return True

if __name__ == "__main__":
    main()
