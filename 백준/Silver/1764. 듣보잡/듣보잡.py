import sys
from copy import deepcopy
inp = sys.stdin.readline

N, M = map(int, inp().split())
s1 = set(inp().replace('\n', '') for _ in range(N))
s2 = set(inp().replace('\n', '') for _ in range(M))

ans = list(s1 & s2)
ans.sort()
print(len(ans))

if len(ans) > 0:
    for a in ans:
        print(a)
