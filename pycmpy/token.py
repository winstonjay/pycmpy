"""token.py:
Define the tokens types to be used by the scanner.
"""
from collections import namedtuple

Token = namedtuple('Token', ("name", "literal", "line"))

EOF     = "eof"
ILLEGAL = "illegal"
INT     = "int"
ID_VAL  = "id"
STRING  = "string"

COMMENT = "#"

#### Operators and delimeters.

LPAREN  = "lparen"  # (
RPAREN  = "rparen"  # )
ADD     = "add"     # +
SUB     = "sub"     # -
MUL     = "mul"     # *
DIV     = "div"     # /
SEMI    = "semi"

operators = {
    '+': ADD,
    '-': SUB,
    '*': MUL,
    '/': DIV,
    '(': LPAREN,
    ')': RPAREN,
    ';': SEMI
}

op_names = set([ADD, SUB, MUL, DIV])

#### Keywords

VAR     = "var"
LET     = "let"
IF      = "if"   
ELSE    = "else"    
PRINT   = "print"
READ    = "read" 

keywords = {
    "var": VAR,
    "let":    LET,
    "if":     IF,
    "else":   ELSE,
    "print":  PRINT
}
