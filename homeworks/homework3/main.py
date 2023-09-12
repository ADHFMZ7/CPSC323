import sys
from enum import Enum
from dataclasses import dataclass
import re

class TokenType(Enum):
    NUMBER = 1
    IDENTIFIER = 2
    KEYWORD = 3
    INVALID = 4

@dataclass
class Token:
    t_type: TokenType 
    contents: str 

def tokenize(file, keywords):

    identifier = re.compile('[a-zA-Z_][a-zA-Z0-9_]*')

    tokens = []
    for line in file:
        for token in line.split():
            if token in keywords:
                t_type = TokenType.KEYWORD
            elif re.fullmatch(identifier, token):
                t_type = TokenType.IDENTIFIER
            elif token.isnumeric():
                t_type = TokenType.NUMBER
            else:
                t_type = TokenType.INVALID
            tokens.append(Token(t_type, token))
    return tokens

def main():


    file = open(sys.argv[1] if len(sys.argv) > 1 else "input", "r")

    keywords = ["while", "for", "switch", "do", "return"]

    tokens = tokenize(file, keywords)

    fstr = "{:<12} {:<10} {:<10} {:<10}" 

    print (fstr.format("Token", "Number", "Identifier", "Keyword"))
    for token in tokens:

        print (fstr.format(token.contents, 
                           "yes" if token.t_type == TokenType.NUMBER else "no", 
                           "yes" if token.t_type == TokenType.IDENTIFIER else "no", 
                           "yes" if token.t_type == TokenType.KEYWORD else "no", 
                           ))

if __name__ == "__main__":
    main()
