import sys
from copy import deepcopy
inp = sys.stdin.readline

def GCD(a, b):
    while b:
        a, b = b, a % b

    return a

a, b = map(int, inp().split())

print((a * b) // GCD(a, b))