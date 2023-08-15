import sys
inp = sys.stdin.readline

T = int(inp())
St = [list(map(int, inp().split())) for _ in range(T)]
St.sort(key = lambda x: (x[0], x[1]))
for k in St:
    print(*k)