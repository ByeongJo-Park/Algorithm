for _ in range(1, 11):
    tc, root = map(int, input().split())
    root_list = list(map(int, input().split()))
    can_go = []
    for k in range(0, len(root_list), 2):
        root = []
        root.append(root_list[k])
        root.append(root_list[k + 1])
        can_go.append(root)
    lc = len(can_go)
    gp = [[0] * 100 for _ in range(100)]
    visit = [False for _ in range(100)]
    for i in can_go:
        u = i[0]
        v = i[1]
        gp[u][v] = 1

    def dfs(v):
        global visit
        visit[v] = True
        for u in range(100):
            if visit[u] == True:
                continue
            if gp[v][u] == 1:
                dfs(u)
    dfs(0)
    print(f'#{tc} {int(visit[99])}')
