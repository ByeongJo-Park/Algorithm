import sys
from copy import deepcopy
inp = sys.stdin.readline

T = int(inp())

def GCD(a, b):
    while b:
        a, b = b, a % b

    return a

for _ in range(T):
    a, b = map(int, inp().split())

    print((a * b) // GCD(a, b))