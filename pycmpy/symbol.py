
import collections

class SymbolTable(object):

    def __init__(self):
        self.table = collections.OrderedDict()

        # define some build in types and functions.
        self.define(BuiltinSymbol("int"))
        self.define(BuiltinSymbol("char"))
        self.define(BuiltinSymbol("void"))
        self.define(FunctionSymbol("print", arglen=1))

    def define(self, symbol):
        print("<define: '%s'>" % symbol.name)
        self.table[symbol.name] = symbol

    def lookup(self, name):
        print("<lookup: '%s'>" % name)
        return self.table.get(name)

    def exists(self, name):
        return self.table.get(name) is not None


class Symbol(object):
    def __init__(self, name, _type=None):
        self.name = name
        self.type = _type

class VarSymbol(Symbol):
    def __str__(self):
        return "<{}:{}>".format(self.name, self.type)

class BuiltinSymbol(Symbol):
    def __str__(self):
        return self.name


class FunctionSymbol(Symbol):
    def __init__(self, name, _type=None, arglen=varadic_len, argtypes=[]):
        self.name = name
        self.type = _type
        self.arglen   = arglen
        self.argtypes = argtypes

    def __str__(self):
        return "<{}:{}>".format(self.name, self.type)

varadic_len = -1