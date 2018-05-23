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
        self.char = text[pos]
        self.pos  = pos
        self.line = line

    def scan(self):
        "return next (token name, token literal, line position)."
        while self.char is not None:
            # first skip whitespace keeping track of newlines by
            # advancing and going back to start of the loop.
            if self.char.isspace():
                if self.char in ('\n', '\r'):
                    self.line += 1
                self._advance()
                continue
            # next if we encounter a single line comment token
            # then skip till a new line is seen and go back to start.
            if self.char == token.COMMENT:
                self._skip_single_comment()
                continue
            # We now expect to see some form of token. check char and
            # branch to the corresponding function. All scan functions
            # are responsible for incrementing the current char position.
            # if we dont find anything return a error (illegal token).
            name, literal = (
                self._scan_operator() if self.char in token.operators else
                self._scan_number() if self.char.isdigit() else
                self._scan_string() if self.char == '"' else
                self._scan_identifier() if self.char.isalpha() else
                self._illegal_token())
            return token.Token(name, literal, self.line)
        # current token is None so we have reached the end of input.
        return token.Token(token.EOF, token.EOF, self.line)

    def _scan_number(self):
        """_advance whilst valid digit chars are seen. [0-9]
        return token.INT with a numeric literal."""
        start = self.pos
        while self.char and self.char.isdigit():
            self._advance()
        return (token.INT, self.text[start:self.pos])

    def _scan_identifier(self):
        """_advance whilst valid alphanumeric chars are seen. check if the
        literal created is a keyword if it is return a (<keyword>, literal)
        if not return a (token.ID_Val, literal)"""
        start = self.pos
        while self.char and self.char.isalnum():
            self._advance()
        literal = self.text[start:self.pos]
        return (token.keywords.get(literal, token.ID_VAL), literal)

    def _scan_operator(self):
        "return opertator token name and literal."
        literal = self.char
        self._advance()
        return (token.operators[literal], literal)

    def _scan_string(self):
        self._advance()
        start = self.pos
        while self.char and self.char not in ('"', '\n'):
            self._advance()
        if self.char != '"':
            self._illegal_token()
        self._advance()
        return (token.STRING, self.text[start:self.pos-1])

    def _skip_single_comment(self):
        "_advance the read char unitl we encounter a newline."
        while self.pos < self.size and self.char not in ('\n', '\r'):
            self.pos += 1
            self.char = self.text[self.pos]
        self.line += 1
        self._advance()

    def _advance(self):
        "Increment read char position or set to None if at end of input"
        try:
            self.pos += 1
            self.char = self.text[self.pos]
        except:
            self.char = None

    def _illegal_token(self):
        literal = self.char
        self._advance()
        return (token.ILLEGAL, literal)
