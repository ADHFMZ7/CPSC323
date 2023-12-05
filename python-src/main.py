from parser import parse_expressions
from tokenizer import tokenize_source
from generate import generate_code
import sys

def main():

    if len(sys.argv) <= 1:
        print(f"Usage: python3 {sys.argv[0]} [expression]")
        return False

    with open(sys.argv[1]) as file_text:
        input_string = file_text.read()

    tokens = tokenize_source(input_string)
  
    if parse_expressions(tokens, all_errors='-e' in sys.argv or '--show-all-errors' in sys.argv):
        generate_code(tokens)
    

if __name__ == "__main__":
    main()
