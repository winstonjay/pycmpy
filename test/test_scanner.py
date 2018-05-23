import sys
sys.path.append("../")

from pycmpy import token
from pycmpy import scanner

try:
    input = raw_input
except:
    pass


def dump_tokens(string):
    s = scanner.Scanner(string)
    t = s.next_token()
    while t.name != token.EOF:
        print(t)
        t = s.next_token()

if __name__ == "__main__":
    while True:
        dump_tokens(input("> "))


