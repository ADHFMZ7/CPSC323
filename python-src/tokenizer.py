from dataclasses import dataclass

@dataclass
class Token:
    lexeme: str
    type:   str
    line:   int

class Scanner:
    def __init__(self, source):
        self.source = source
        self.tokens = []

        self.start = 0
        self.current = 0
        self.line = 1

    def next_char(self):
        self.current += 1
        return self.source[self.current - 1]

    def peek(self):
        return self.source[self.current]

    def add_token(self, type):
        self.tokens.append(
                Token(self.substr(),
                      type,
                      self.line))
        print(self.tokens[-1])

    def substr(self):
        return self.source[self.start:self.current]

def tokenize_source(source: str):

    tokens = []

    scanner = Scanner(source)

    while scanner.current < len(source):
        
        char = scanner.next_char()

        while char.isspace():
            if char == '\n':
                scanner.line += 1
            scanner.start = scanner.current
            char = scanner.next_char()

        if char == "(":
            if scanner.peek() == '*':
                scanner.next_char()
                while scanner.next_char() != '*' and scanner.peek() != ')':
                    scanner.line += scanner.peek() == '\n'
            else:
                scanner.add_token('(')

        elif char in "),;:=+-*/":
            scanner.add_token(char) 


        elif char == '"':
            pass

        elif char.isalnum():
            while scanner.peek().isalnum():
                scanner.next_char()
        
            if scanner.substr() == "end" and scanner.peek() == '.':
                scanner.next_char()
            scanner.add_token(scanner.substr()) 




