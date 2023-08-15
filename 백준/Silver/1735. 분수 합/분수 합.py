import sys
from copy import deepcopy
inp = sys.stdin.readline

def G(a, b):
    while b:
        a, b = b, a % b

    return a

a, b = map(int, inp().split())
c, d = map(int, inp().split())

head = (a * d) + (b * c)
bot = b * d
print(f'{head//G(head, bot)} {bot//G(head, bot)}')