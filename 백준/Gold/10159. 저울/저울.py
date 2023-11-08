N = int(input())

M = int(input())

L = [[0 for p in range(N)] for __ in range(N)]

for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    L[x][y] = 1

for a in range(N):
    for b in range(N):
        for c in range(N):
            if L[b][a] and L[a][c]:
                L[b][c] += 1

for i in range(N):
    cnt = 0
    for j in range(N):
        if not L[i][j] and not L[j][i] and i != j:
            cnt += 1
    print(cnt)