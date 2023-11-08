from collections import deque

N, M = map(int, input().split())

board = [0 for _ in range(100)]
visit = [False for _ in range(100)]
SADARY = dict()
BAM = dict()

start = 0
end = 99

for i in range(N):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    SADARY[x] = y

for i in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    BAM[x] = y

q = deque([])
q.append(start)
while q:
    point = q.popleft()
    if point == end:
        print(board[end])
        break

    for d in range(1, 7):
        n = point + d
        if n < 100 and not visit[n]:
            if n in SADARY.keys():
                n = SADARY[n]
            if n in BAM.keys():
                n = BAM[n]
            if not visit[n]:
                visit[n] = True
                board[n] = board[point] + 1
                q.append(n)
