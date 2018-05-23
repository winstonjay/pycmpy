
import sys
sys.path.append("../")
from pycmpy import parser
from pycmpy import scanner


text = '''
int y;
int x = - + - 1 + 3 * 2;
char z = "hello";
// int main() { ; } not implemented yet and this is commented out
int a = 100; // i am another comment
print(1, 2, 3);
int a = pow(20, x);
print("goodbye");
;;
'''

s   = scanner.Scanner(text)
p   = parser.Parser(s)
ast = p.parse()


print(ast)