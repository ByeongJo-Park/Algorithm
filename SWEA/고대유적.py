T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    map_list = [list(map(int, input().split())) for _ in range(N)]
    trans_map = list(map(list, zip(*map_list)))
    ans = []
    for i in range(N):
        leng = 0
        for j in range(M):
            if map_list[i][j] == 1:
                leng += 1
                if j == M-1:
                    ans.append(leng)
            elif map_list[i][j] == 0:
                if leng != 0:
                    ans.append(leng)
                    leng = 0

    for l in range(M):
        leng = 0
        for k in range(N):
            if trans_map[l][k] == 1:
                leng += 1
                if k == N-1:
                    ans.append(leng)
            elif trans_map[l][k] == 0:
                if leng != 0:
                    ans.append(leng)
                    leng = 0
    print(f'#{tc} {max(ans)}')