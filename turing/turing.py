


def next_right(string, index, char):

    for i in range(index+1, len(string)):
        if string[i] == char:
            return i 
    return len(string)

def next_left(string, index, char):
    for i in range(index - 1, -1, -1):
        if string[i] == char:
            return i
    return -1


def sc(input_str, index, new_char):
    if 0 <= index < len(input_str):
        # Create a new string with the desired character replaced
        modified_str = input_str[:index] + new_char + input_str[index + 1:]
        return modified_str
    else:
        # Index out of range
        return input_str


def main():

    inp = input("enter string: ")

    input_string = f"#{inp}#######"

    print(input_string)
    

    head = next_right(input_string, 0, '#')

    while input_string[head-1] != '#':
        head -= 1
        r = input_string[head]

        input_string = sc(input_string, head, '#')

        head = next_right(input_string, head, '#')
        head = next_right(input_string, head, '#')

        input_string = sc(input_string, head, r)

        head = next_left(input_string, head, '#')
        head = next_left(input_string, head, '#')

        input_string = sc(input_string, head, r)

        print(input_string)
        

    print(input_string)

if __name__ == "__main__":

    main()


