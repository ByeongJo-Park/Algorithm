import sys
inp = sys.stdin.readline

N, M = map(int, inp().split())

N_l = {inp().replace('\n', '') : 1 for _ in range(N)}
M_l = list(inp().replace('\n', '') for _ in range(M))
cnt = 0

for m in M_l:
    if m in N_l:
        cnt += 1

print(cnt)