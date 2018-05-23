

class NodeVisitor(object):

    def visit(self, node):
        name = "visit_{}".format(type(node).__name__)
        func = getattr(self, name, self.generic_visit)
        return func(node)

    def generic_visit(self, node):
        raise Exception("No visit_{} method".format(type(node).__name__))



class AST(object):
    "AST provides a base class for our syntax tree"
    pass


class Program(AST):
    def __init__(self):
        self.statements = []

    def __str__(self):
        s = ";\n\t".join("%s" % s for s in self.statements)
        return "program:\n\t{};".format(s)


class Statment(AST):
    def __init__(self, statement):
        self.statement = statement

# class FuncDecl(AST):
#     def __init__(self, token, name, args, body):
#         self.token = token.

class FuncCall(AST):
    def __init__(self, token, args):
        self.token = token
        self.name = token.value
        self.args = args

    def __str__(self):
        return "<func:'%s'>%s" % (self.name, self.args)

class If(AST):
    def __init__(self, token, statment):
        self.token = token
        self.statement = statment

class VarAssign(AST):
    def __init__(self, _type, var, value):
        self.type = _type
        self.var = var
        self.value = value

    def __str__(self):
        return "<%s:'%s'> = %s" % (self.type.value,
                                 self.var.value,
                                 self.value)

class VarDecl(AST):
    def __init__(self, _type, var):
        self.type = _type
        self.var = var

    def __str__(self):
        return "<%s:'%s'>" % (self.type.value, self.var.value)


class ExprList(AST):
    def __init__(self, token):
        self.token = token
        self.exprs = []

    def __str__(self):
        exprs = ", ".join("%s" % e for e in self.exprs)
        l = self.token.value
        r = {"(": ")", "{": "}"}[l]
        return "%s%s%s" % (l, exprs, r)


class BinaryOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = op
        self.op = op.value
        self.right = right

    def __str__(self):
        return "(%s %s %s)" % (self.left, self.op, self.right)

    __repr__ = __str__

class UnaryOp(AST):
    def __init__(self, op, expr):
        self.token = op
        self.op = op.value
        self.expr = expr

    def __str__(self):
        return "(%s %s)" % (self.op, self.expr)

    __repr__ = __str__

class NoOp(AST):
    pass

# atoms all have the same structure.

class Atom(AST):
    def __init__(self, tok):
        self.token = tok
        self.value = tok.value

    def __str__(self):
        return self.token.value

class NumberConst(Atom): pass
class StringConst(Atom): pass
class Type(Atom):        pass

class Var(Atom):
    def __str__(self):
        return "<var:'{}'>".format(self.value)