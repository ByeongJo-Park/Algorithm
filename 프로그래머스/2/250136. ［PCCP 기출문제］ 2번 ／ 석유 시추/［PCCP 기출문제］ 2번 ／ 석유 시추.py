from collections import deque
def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    visited = [[0 for i in range(m)] for j in range(n)]
    gas = [ 0 for _ in range(m+1)]
    def bfs(a, b):
        count = 0
        visited[a][b] = 1
        q1 = deque()
        q1.append((a,b))
        mn, mx = b, b
        while q1:
            x,y = q1.popleft()
            mn = min(mn, y)
            mx = max(mx, y)
            count += 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if visited[nx][ny] == 0 and land[nx][ny] == 1:
                    visited[nx][ny] = 1
                    q1.append((nx,ny))

        for i in range(mn, mx+1):
            gas[i] += count

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and land[i][j] == 1:
                bfs(i,j)

        answer = max(gas)
    return answer