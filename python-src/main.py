from parser import parse_expressions
from tokenizer import tokenize_source
from generate import generate_code
import os
import sys

def main():

    if len(sys.argv) <= 1:
        print(f"Usage: python3 {sys.argv[0]} [filename]")
        return False

    out_file = "main.c" if '-o' not in sys.argv else sys.argv[sys.argv.index('-o')+ 1]

    with open(sys.argv[1]) as file_text:
        input_string = file_text.read()

    tokens = tokenize_source(input_string)
  
    if parse_expressions(tokens, all_errors='-e' in sys.argv or '--show-all-errors' in sys.argv) == 1:
        if generate_code(tokens, out_file, all_errors='-e' in sys.argv or '--show-all-errors' in sys.argv):
            print("File saved in", out_file)
            return True
    
        os.remove(out_file)

    print("Failed to compile") 

if __name__ == "__main__":
    main()
