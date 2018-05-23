'''
parser.py

stack based parser converting infix expressions to post-fix.
This is passed on to the Emitter which may produce its own errors.
'''
import token
import ast


class Parser(object):

    def __init__(self, scanner):
        self.scanner = scanner
        self.errors  = []
        self.peek = self.scanner.next_token()

    def parse(self):
        ast = self.parse_program()
        if self.errors:
            self.dump_errors()
            return None
        return ast

    def parse_program(self):
        program = ast.Program()
        while self.peek.type != token.EOF:
            stmt = self.statement()
            self.match(token.SEMI)
            program.statements.append(stmt)
        return program

    def statement(self):
        if self.peek.type == token.ILLEGAL:
            self.error("Illegal Token/unexpected end of string")
            return None
        types = (token.INT, token.CHAR, token.VOID)
        return (self.assign() if self.peek.type in types else
                ast.NoOp if self.peek.type == token.SEMI else
                self.expr())

    def assign(self):
        var_type = self.peek
        if var_type.type == token.INT:
            self.match(token.INT)
        elif var_type.type == token.CHAR:
            self.match(token.CHAR)
        elif var_type.type == token.VOID:
            self.match(token.CHAR)
        var = self.symbol()
        if self.peek.type != token.ASSIGN:
            return ast.VarDecl(var_type, var)
        self.match(token.ASSIGN)
        return ast.VarAssign(var_type, var, self.expr())

    def expression_list(self, delim):
        '''ExprList = Expr , ExprList
                    | Expr'''
        expressions = ast.ExprList(delim)
        self.match(token.LPAREN)
        while self.peek.type not in (token.EOF, token.RPAREN):
            expressions.exprs.append(self.expr())
            if self.peek.type == token.COMMA:
                self.match(token.COMMA)
            else:
                self.match(token.RPAREN)
                break
        return expressions

    def expr(self):
        node = self.term()
        while self.peek.type in (token.ADD, token.SUB):
            tok = self.peek
            if tok.type == token.ADD:
                self.match(token.ADD)
            elif tok.type == token.SUB:
                self.match(token.SUB)
            node = ast.BinaryOp(node, tok, self.term())
        return node

    def term(self):
        "term = term * factor | term / factor"
        node = self.factor()
        while self.peek.type in (token.STAR, token.SLASH):
            tok = self.peek
            if tok.type == token.STAR:
                self.match(token.STAR)
            elif tok.type == token.SLASH:
                self.match(token.SLASH)
            node = ast.BinaryOp(node, tok, self.factor())
        return node

    def factor(self):
        '''
        factor  = UnaryOp | ( Expr ) | FuncCall | Atom
        UnaryOp = - Expr | + Expr
        Atom    = Number_const | String_const | Symbol
        '''
        tok = self.peek
        if tok.type == token.ADD:
            self.match(token.ADD)
            return ast.UnaryOp(tok, self.factor())
        elif tok.type == token.SUB:
            self.match(token.SUB)
            return ast.UnaryOp(tok, self.factor())
        elif tok.type == token.LPAREN:
            self.match(token.LPAREN)
            node = self.expr()
            self.match(token.RPAREN)
            return node
        elif tok.type == token.NUMBER_CONST:
            self.match(token.NUMBER_CONST)
            return ast.NumberConst(tok)
        elif tok.type == token.STRING_CONST:
            self.match(token.STRING_CONST)
            return ast.StringConst(tok)
        elif tok.type == token.SYMBOL:
            node = self.peek
            self.match(token.SYMBOL)
            if self.peek.type == token.LPAREN:
                return self.func_call(node)
            return ast.Var(node)
        else:
            raise Exception("Unexpected token.")

    def func_call(self, name):
        "FuncCall = Symbol ( ExprList )"
        delim = self.peek
        args  = self.expression_list(delim)
        return ast.FuncCall(name, args)

    def symbol(self):
        tok = self.peek
        self.match(token.SYMBOL)
        return ast.Var(tok)

    def match(self, tok):
        if self.peek.type != tok:
            n = token.token_names
            raise Exception("Wrong token got=%s. want=%s" % (
                            n[self.peek.type], n[tok]))
        self.peek = self.scanner.next_token()
