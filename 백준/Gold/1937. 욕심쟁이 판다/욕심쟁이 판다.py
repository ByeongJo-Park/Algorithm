import sys
input = sys.stdin.readline
# 재귀맥스 열어놓기...500 * 500 을 모두 갈수 있다고 했을때 최소 25000
sys.setrecursionlimit(25000)
# dfs를 이용
def dfs(i, j):
    global dp
    if dp[i][j]:
        return dp[i][j]
    dp[i][j] = 1
    for k in range(4):
        di, dj = i + d[k][0], j + d[k][1]
        if (0 <= di < N and 0 <= dj < N) and panda_map[i][j] < panda_map[di][dj]:
            dp[i][j] = max(dp[i][j], dfs(di, dj) + 1)
    return dp[i][j]


d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
N = int(input().rstrip())
panda_map = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
answer = 0

for i in range(N):
    for j in range(N):
        answer = max(dfs(i, j), answer)

print(answer)