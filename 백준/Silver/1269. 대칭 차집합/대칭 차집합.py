import sys
from copy import deepcopy
inp = sys.stdin.readline

N, M = map(int, inp().split())
s1 = set(map(int, inp().split()))
s2 = set(map(int, inp().split()))
ans1 = set(s1 | s2)
ans2 = set(s1 & s2)
ans = set(ans1 - ans2)
print(len(ans))
