def dfs():
    global ans
    if len(s) == m:
        # k = sorted(list(s))
        # if k not in ans:
        ans.append(list(s))
        return
    for i in range(1, n + 1):
        if visited[i]:
            continue
        s.append(i)
        dfs()
        s.pop()


n, m = map(int, input().split())
s = []
ans = []
visited = [False] * (n + 1)

dfs()
for i in range(len(ans)):
    print(*ans[i])