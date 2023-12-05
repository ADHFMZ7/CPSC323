
keywords = ["program", "var", "begin", "end.", "integer", "write"]

table = {
    'A': {"program": "program B ; var D begin H end.", },
    'B': {"LET": "V C"},
    'C': {";": "_", ':': "_", ',': "_", ')': "_", '=': '_', '+': '_','-': '_','*': '_','/': '_', 'NUM':'U C', 'LET':'V C'},
    'D': {'LET': 'E : G ;'},
    'E': {'LET': 'B F'},
    'F': {':':'_', ',':'B F' },
    'G': {'integer':'integer'},
    'H': {'write': 'J I', 'LET': 'J I'},
    'I': {'end.': '_', 'write': 'J I', 'LET': 'J I'},
    'J': {'write': 'K', "LET": "M"},
    'K': {"write": "write ( L B ) ;"},
    'L': {'"value=",': '"value=",', "LET": "_"},
    'M': {'LET': "B = N ;"},
    'N': {'(': 'P O', '+': 'P O', '-': 'P O', 'LET': 'P O', 'NUM': 'P O'},
    'O': {';': "_", ')': '_', '+':'+ P O', '-':'- P O'},
    'P': {'(': 'R Q', '+':'R Q', '-': 'R Q', 'NUM': 'R Q', 'LET': 'R Q'},
    'Q': {';': '_', ')': '_', '+': '_', '-': '_', '*': '* R Q', '/': '/ R Q'},
    'R': {'(':'( N )', '+': 'S', '-': 'S', 'NUM': 'S', 'LET': 'B'},
    'S': {'+': 'T U W', '-': 'T U W', 'NUM': 'T U W'},
    'T': {'+': '+', '-': '-', 'NUM': '_'},
    'U': {'NUM': 'NUM'},
    'V': {'LET': 'LET'},
    'W': {';': '_', ')': '_', '+': '_', '-':'_', '*':'_', '/':'_', 'NUM':'U W'},
}

def lookup(row, column):
  
    t = table[row]
    return t.get(column, 0)
