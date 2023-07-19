N, M = map(int, input().split())
T = []
for t in range(0,N):
    T.append(0)

for i in range(0,M):
    a, b, c = map(int, input().split())
    for k in range(a, b + 1):
        T[k-1] = c

print(*T)    