import sys
sys.path.append("../")
from pycmpy import scanner
from pycmpy import parser
from pycmpy import analyzer

text = "int u; int x = 100; print(\"hello\");"
s   = scanner.Scanner(text)
p   = parser.Parser(s)
tree = p.parse()

a = analyzer.SemanticAnalyzer()

a.visit(tree)

