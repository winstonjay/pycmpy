"""token.py:
Define the token types to be used by the scanner.

'A token is a pair consisting of a token name and an optional attribute
value. The token name is an abstract symbol representing a kind of lexical
unit, e.g., a particular keyword, or sequence of input characters denoting
an identifier. The token names are the input symbols that the parser
processes' (p.111).

'A lexeme is a sequence of characters in the source program that matches
the pattern for a token and is identified by the lexical analyzer as an
instance of that token' (p.111).

Ref: (Aho, Lam, Sethi and Ullman. 2007.
      Compilers: Principles, Techniques, and Tools. 2nd ed.)
"""


class Token(object):
    '''Represents a lexical unit denoted by a token type (int) and string
    literal value. Comparisons between tokens are made by their type.
    '''
    def __init__(self, _type, value):
        self.type = _type
        self.value = value

    def __str__(self):
        "String repr primarly for debugging."
        name = token_names[self.type]
        return "Token<{}: '{}'>".format(name, self.value)

    __repr__ = __str__

    # Enable equality testing of token type (int) with other int values.
    def __eq__(self, other): return self.type == other
    def __ne__(self, other): return self.type != other

    def __hash__(self):      return self.type


# Define token types by enumeration. Any additions need to be reflected in the
# range count and within the name map, defined after.
(EOF,           # EOF
 ILLEGAL,       # ILLEGAL
 VOID,          # void
 INT,           # int
 CHAR,          # char
 SYMBOL,        # alphanumeric identifier
 INT_CONST,     # any integer
 CHAR_CONST,    # " any string "
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


# Map string representations of token names primarily for debugging purposes.
# These will be seen in error reports for the user, tests, etc.
token_names = {
    EOF:        "EOF",
    ILLEGAL:    "ILLEGAL",
    VOID:       "VOID",
    INT:        "INT",
    CHAR:       "CHAR",
    SYMBOL:     "SYMBOL",
    INT_CONST:  "INT_CONST",
    CHAR_CONST: "CHAR_CONST",
    LPAREN:     "LPAREN",
    RPAREN:     "RPAREN",
    LSQR:       "LSQR",
    RSQR:       "RSQR",
    LCURL:      "LCURL",
    RCURL:      "RCURL",
    ADD:        "ADD",
    SUB:        "SUB",
    STAR:       "STAR",
    SLASH:      "SLASH",
    LTHAN:      "LTHAN",
    GTHAN:      "GTHAN",
    EQUAL:      "EQUAL",
    ASSIGN:     "ASSIGN",
    SEMI:       "SEMI",
    COMMA:      "COMMA",
    IF:         "IF",
    ELSE:       "ELSE"
}

keywords = {
    "int":    INT,
    "char":   CHAR,
    "void":   VOID,
    "if":     IF,
    "else":   ELSE
}