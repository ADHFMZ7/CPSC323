from table import keywords


# def report_gen_error(message, token):
#     print(f"Error:{token.line}: {message}")
#     
# def report_parse_error(message, token, state):
#
#     if state in ";,.()" or state in keywords:
#         print(f"Error: {message} on line {token.line}. expected <{state}>, recieved <{token.lexeme}>")
#     else:
#         print(f"Error: {message} on line {token.line}. <{token.type}>")
#
#
#
# def report_token_error(lexeme, line):
#     print(f"Error: Unrecognized token <{lexeme}> on line {line}")
#
#

from table import keywords

def report_gen_error(message, token):
    print(f"\033[91mError:\033[0m {message}. (line {token.line})")

def report_parse_error(message, token, state):
    if state in ";,.()" or state in keywords:
        print(f"\033[91mError:\033[0m {message}. expected <{state}>, received <{token.lexeme}> (line {token.line})")
    else:
        print(f"\033[91mError:\033[0m {message}. <{token.type}> (line {token.line})")

def report_token_error(lexeme, line):
    print(f"\033[91mError:\033[0m Unrecognized token <{lexeme}>. (line {line})")

