'''
scanner.py:

Define the class Scanner which is responosible for peforming lexical anaylsis
of source code. It is incrementally called by the parser emiting a token,
literal and line number each time.
'''
import token

class Scanner(object):
    '''
    Scanner implements methods for conducting a lexical analysis of source
    codes, keeping track of its own state.
    '''
    def __init__(self, text, pos=0, line=0):
        self.text = text
        self.size = len(text) - 1
        self.pos  = -1
        self.advance()
        self.line = line

    def next_token(self):
        "return next Token."
        while self.char is not None:
            # first skip whitespace keeping track of newlines by
            # advancing and going back to start of the loop.
            if self.char.isspace():
                if self.char in ('\n', '\r'):
                    self.line += 1
                self.advance()
                continue
            # next if we encounter a single line comment token
            # then skip till a new line is seen and go back to start.
            if self.char == "/":
                self.advance()
                if self.char != "/":
                    return token.Token(token.SLASH, "/")
                self._skip_single_comment()
                continue
            # We now expect to see some form of token. check char and
            # branch to the corresponding function. All scan functions
            # are responsible for incrementing the current char position.
            # if we dont find anything return a error (illegal token).
            if self.char == "(":
                self.advance()
                return token.Token(token.LPAREN, "(")
            elif self.char == ")":
                self.advance()
                return token.Token(token.RPAREN, ")")
            elif self.char == "[":
                self.advance()
                return token.Token(token.LSQR, "[")
            elif self.char == "]":
                self.advance()
                return token.Token(token.RSQR, "]")
            elif self.char == "{":
                self.advance()
                return token.Token(token.LCURL, "{")
            elif self.char == "}":
                self.advance()
                return token.Token(token.RCURL, "}")
            elif self.char == "+":
                self.advance()
                return token.Token(token.ADD, "+")
            elif self.char == "-":
                self.advance()
                return token.Token(token.SUB, "-")
            elif self.char == "*":
                self.advance()
                return token.Token(token.STAR, "*")
            elif self.char == "<":
                self.advance()
                return token.Token(token.LTHAN, "<")
            elif self.char == ">":
                self.advance()
                return token.Token(token.GTHAN, ">")
            elif self.char == "=":
                self.advance()
                if self.char != "=":
                    return token.Token(token.ASSIGN, "=")
                self.advance()
                return token.Token(token.EQUAL, "==")
            elif self.char == ";":
                self.advance()
                return token.Token(token.SEMI, ";")
            elif self.char == ",":
                self.advance()
                return token.Token(token.COMMA, ",")
            else:
                return token.Token(*
                        self.string() if self.char == '"'    else
                        self.number() if self.char.isdigit() else
                        self.symbol() if self.char.isalpha() else
                        self.illegal_token())
        # current token is None so we have reached the end of input.
        return token.Token(token.EOF, token.EOF)

    def number(self):
        """advance whilst valid digit chars are seen. [0-9]
        return token.INT with a numeric literal."""
        start = self.pos
        while self.char and self.char.isdigit():
            self.advance()
        return (token.NUMBER_CONST, self.text[start:self.pos])

    def symbol(self):
        """advance whilst valid alphanumeric chars are seen. check if the
        literal created is a keyword if it is return a token.<keyword>
        if not return a token.SYMBOL"""
        start = self.pos
        while self.char and self.char.isalnum():
            self.advance()
        literal = self.text[start:self.pos]
        return (token.keywords.get(literal, token.SYMBOL), literal)

    def string(self):
        self.advance() # skip pass the start quote "
        start = self.pos
        while self.char and self.char not in ('"', '\n'):
            self.advance()
        if self.char != '"':
            self.illegal_token()
        self.advance() # skip pass the end quote "
        return (token.STRING_CONST, self.text[start:self.pos-1])

    def _skip_single_comment(self):
        "advance the read char unitl we encounter a newline."
        while self.pos < self.size and self.char not in ('\n', '\r'):
            self.pos += 1
            self.char = self.text[self.pos]
        self.line += 1
        self.advance()

    def advance(self):
        "Increment read char position or set to None if at end of input"
        try:
            self.pos += 1
            self.char = self.text[self.pos]
        except:
            self.char = None

    def illegal_token(self):
        literal = self.char
        self.advance()
        return (token.ILLEGAL, literal)
