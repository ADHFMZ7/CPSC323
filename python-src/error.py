from table import keywords


def report_parse_error(message, token, state):

    if state in ";,.()" or state in keywords:
        print(f"Error: {message} on line {token.line}. expected <{state}>, recieved <{token.lexeme}>")
    else:
        print(f"Error: {message} on line {token.line}. <{token.type}>")



def report_token_error(lexeme, line):
    print(f"Error: Unrecognized token <{lexeme}> on line {line}")
