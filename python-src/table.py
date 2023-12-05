
keywords = ["program", "var", "begin", "end.", "integer", "write"]

table = {
    'A': {"program": "program B ; var D begin H end.", },
    'B': {"B": "V C"},
    'C': {";": "_", ':': "_", ',': "_", ')': "_", '=': '_', '+': '_','-': '_','*': '_','/': '_', 'S':'U C', 'B':'V C'},
    'D': {'B': 'E : G ;'},
    'E': {'B': 'B F'},
    'F': {':':'_', ',':', B F' },
    'G': {'integer':'integer'},
    'H': {'write': 'J I', 'B': 'J I'},
    'I': {'end.': '_', 'write': 'J I', 'B': 'J I'},
    'J': {'write': 'K', "B": "M"},
    'K': {"write": "write ( L B ) ;"},
    'L': {'STRING': 'STRING', "B": "_"},
    'M': {'B': "B = N ;"},
    'N': {'(': 'P O', '+': 'P O', '-': 'P O', 'B': 'P O', 'S': 'P O'},
    'O': {';': "_", ')': '_', '+':'+ P O', '-':'- P O'},
    'P': {'(': 'R Q', '+':'R Q', '-': 'R Q', 'S': 'R Q', 'B': 'R Q'},
    'Q': {';': '_', ')': '_', '+': '_', '-': '_', '*': '* R Q', '/': '/ R Q'},
    'R': {'(':'( N )', '+': 'S', '-': 'S', 'S': 'S', 'B': 'B'},
    'S': {'+': 'T U W', '-': 'T U W', 'S': 'T U W'},
    'T': {'+': '+', '-': '-', 'S': '_'},
    'U': {'S': 'S'},
    'V': {'B': 'B'},
    'W': {';': '_', ')': '_', '+': '_', '-':'_', '*':'_', '/':'_', 'S':'U W'},
}

def lookup(row, column):
  
    t = table[row]
    return t.get(column, 0)
