import sys
from copy import deepcopy
inp = sys.stdin.readline
def G(x, y):
    while y:
        x, y = y, x % y
    return x

N = int(inp())


k = 0
a1 = int(inp())
b1 = int(inp())
c1 = b1 - a1
d = [c1]
ans = c1
res = 0
while k < N-2:
    a1 = b1
    b1 = int(inp())
    c1 = b1 - a1
    d.append(c1)
    ans = G(ans, c1)
    k += 1

for i in d:
    res += ((i // ans) - 1)

print(res)