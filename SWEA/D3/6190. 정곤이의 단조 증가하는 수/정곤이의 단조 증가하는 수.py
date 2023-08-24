T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num_l = list(map(int, input().split()))
    ans = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            t = num_l[i] * num_l[j]
            st = str(t)
            for k in range(len(st)-1):
                if int(st[k]) > int(st[k + 1]):
                    break
            else:
                ans.append(t)

    print(f'#{tc} {max(ans) if len(ans) != 0 else -1}')