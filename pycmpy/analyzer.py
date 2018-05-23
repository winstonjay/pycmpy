
import ast
import symbol

# https://github.com/rspivak/lsbasi/blob/master/part13/spi.py
# https://www.tutorialspoint.com/compiler_design/compiler_design_semantic_analysis.htm
# https://www.tutorialspoint.com/compiler_design/compiler_design_quick_guide.htm
class SemanticAnalyzer(ast.NodeVisitor):
    '''The SemanticAnalyzer is responsible for checking
    (will be):
    - scope resolution
    - type checking
    - array/param bound checking.
    - identifer declarations (multiple, undeclaried, restricted)'''

    def __init__(self):
        self.symtab = symbol.SymbolTable()

    def visit_Program(self, node):
        for stmt in node.statements:
            self.visit(stmt)

    def visit_Statement(self, node):
        # non existant
        pass

    def visit_VarAssign(self, node):
        type_name = node.type.value
        type_symb = self.symtab.lookup(type_name)

        var_name = node.var.value
        var_symb = symbol.VarSymbol(var_name, type_name)

        if self.symtab.exists(var_name):
            raise Exception("Redfined within the same scope. %s" % var_name)
        self.symtab.define(var_symb)

    def visit_VarDecl(self, node):
        self.visit_VarAssign(node)

    def visit_Var(self, node):
        var_name = node.value
        var_symb = self.symtab.lookup(var_name)
        if var_symb is None:
            raise Exception("Identifier '%s' not found" % var_name)

    def visit_FuncCall(self, node):
        fn_name = node.name
        fn_symb = self.symtab.lookup(fn_name)
        if fn_symb is None:
            raise Exception("Function '%s' not found" % fn_name)

        if (fn_symb.arglen != symbol.varadic_len
            and fn_symb.arglen != len(node.args.exprs)):
            raise Exception("Wrong arg len for '%s'" % fn_name)

        # if fn_symb.argtypes:
        #     for (a, b) in fn_symb.argtypes
