import sys
from copy import deepcopy
inp = sys.stdin.readline

N = int(inp())
d = {}
for _ in range(N):
    a, b = inp().split()
    d[a] = b

name = d.keys()
ans = []
for n in name:
    if d[n] != 'leave':
        ans.append(n)

ans.sort(reverse=True)
for _ in ans:
    print(_)