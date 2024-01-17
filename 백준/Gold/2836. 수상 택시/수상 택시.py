import sys
input = sys.stdin.readline
N, M = map(int, input().split())

rtMove = []

for _ in range(N):
    s, e = map(int, input().split())
    if s > e:
        rtMove.append([e, s])

rtMove.sort(key= lambda x: -x[1])

dist = []

ns, ne = rtMove[0]

for __ in range(1, len(rtMove)):
    cs, ce = rtMove[__]
    if ns <= ce:
        ns = min(ns, cs)
    else:
        dist.append([ns, ne])
        ns, ne = cs, ce

dist.append([ns, ne])

for ___ in range(len(dist)):
    M += 2 * (dist[___][1] - dist[___][0])

print(M)