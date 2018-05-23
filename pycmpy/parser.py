'''
parser.py

stack based parser converting infix expressions to post-fix.
This is passed on to the Emitter which may produce its own errors.
'''
import token
from scanner import Scanner


class Parser(object):
    '''
    Parser implements infix to post-fix expr parsing the results are
    stored in a list and returned at the end. main external method is parse.
    '''
    def __init__(self, scanner):
        self.scanner = scanner
        self.peek = token.Token
        self.errors = []
        self.stack = []
        # init the first token.
        self.peek = self.scanner.scan()

    def parse(self):
        "parse program return stack or errors"
        self.statement_list()
        if self.errors:
            for e in self.errors:
                print(e)
            return [None]
        return self.stack

    def statement_list(self):
        '''statement_list = statement ; statement_list
                          | statement ;
        '''
        while (self.peek.name != token.EOF):
            if not self.statement():
                break
            tok = self.peek
            self.match(token.SEMI)
            self.stack.append(tok)
        self.stack.append(self.peek)
    
     
    def statement(self):
        '''statement = print expr
                     | expr
        '''
        if self.peek.name == token.VAR:
            pass
        elif self.peek.name == token.PRINT:
            tok = self.peek
            self.match(token.PRINT)
            self.expr()
            self.stack.append(tok)
        elif self.peek.name == token.ILLEGAL:
            self.error("Illegal Token/unexpected end of string")
            print(self.error[-1])
            return False
        else:
            self.expr()
        return True

    def expr(self):
        '''expr = expr + term
                | expr - term
                | term
        '''
        self.term()
        while self.peek.literal in ("+", "-"):
            tok = self.peek
            self.match(tok.name)
            self.term()
            self.stack.append(tok)

    def term(self):
        '''term = term * factor
                | term / factor
                | factor
        '''
        self.factor()
        while self.peek.literal in ("*", "/"):
            tok = self.peek
            self.match(tok.name)
            self.factor()
            self.stack.append(tok)

    def factor(self):
        '''factor = ( expr )
                  | id
                  | num
        '''  
        tok = self.peek
        if tok.literal == "(":
            self.match(token.LPAREN)
            self.expr()
            self.match(token.RPAREN)
        elif tok.name in (token.INT, token.ID_VAL, token.STRING):
            self.stack.append(tok)
            self.match(tok.name)
        elif tok.name == token.EOF:
            return
        else:
            return self.error("Illegal Syntax unexpected token {}, '{}'",
                              tok.name, tok.literal)

    def match(self, tok):
        "check if token is correct then advance or throw an error."
        if self.peek.name != tok:
            return self.error("unexpeted token. want={}. got={}",
                         tok, self.peek.name)
        self.peek = self.scanner.scan()

    def error(self, message, *args):
        self.errors.append("Parse Error, Line {}: ".format(self.peek.line)
                           + message.format(*args))
        if len(self.errors) > 3:
            for e in self.errors:
                print(e)
            raise Exception("Too many errors!")
        return None


