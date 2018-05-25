import sys
sys.path.append("../")

from pycmpy import token
from pycmpy import scanner

try:
    input = raw_input
except:
    pass

# at least do some regression tests

def dump_tokens(string):
    s = scanner.Scanner(string)
    t = s.next_token()
    while t.type != token.EOF:
        print(t)
        print("main:{line}:{col}:\n{trace}\n".format(**s.trace(t)))
        t = s.next_token()

if __name__ == "__main__":
    while True:
        dump_tokens(input("> "))



