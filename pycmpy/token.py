"""token.py:
Define the tokens types to be used by the scanner.
"""

class Token(object):

    def __init__(self, _type, value):
        self.type = _type
        self.value = value

    def __str__(self):
        return "Token<{}: '{}'>".format(token_names[self.type], self.value)

    __repr__ = __str__

(EOF,           # EOF
 ILLEGAL,       # ILLEGAL
 VOID,          # void
 INT,           # int
 CHAR,          # char
 SYMBOL,        # alphanumeric identifier
 NUMBER_CONST,  # any integer
 STRING_CONST,  # " any string "
 LPAREN,        # (
 RPAREN,        # )
 LSQR,          # [
 RSQR,          # ]
 LCURL,         # {
 RCURL,         # }
 ADD,           # +
 SUB,           # -
 STAR,          # *
 SLASH,         # /
 LTHAN,         # <
 GTHAN,         # >
 EQUAL,         # ==
 ASSIGN,        # =
 SEMI,          # ;
 COMMA,         # ,
 IF,            # if
 ELSE           # else
) = range(26)

token_names = [
    "EOF",
    "ILLEGAL",
    "VOID",
    "INT",
    "CHAR",
    "SYMBOL",
    "NUMBER_CONST",
    "STRING_CONST",
    "LPAREN",
    "RPAREN",
    "LSQR",
    "RSQR",
    "LCURL",
    "RCURL",
    "ADD",
    "SUB",
    "STAR",
    "SLASH",
    "LTHAN",
    "GTHAN",
    "EQUAL",
    "ASSIGN",
    "SEMI",
    "COMMA",
    "IF",
    "ELSE"
]

keywords = {
    "int":    INT,
    "char":   CHAR,
    "void":   VOID,
    "if":     IF,
    "else":   ELSE
}