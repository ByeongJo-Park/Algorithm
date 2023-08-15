import sys
from copy import deepcopy
inp = sys.stdin.readline

T = int(inp())
T_l = list(map(int, inp().split()))
dic = {T_l[i] : 1 for i in range(T)}

N = int(inp())
N_l = list(map(int, inp().split()))
ans = [0] * N
for n in range(N):
    if dic.get(N_l[n]):
        ans[n] = 1

print(*ans)
