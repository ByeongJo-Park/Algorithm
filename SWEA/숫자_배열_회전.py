def rotate(li, n):
    return_list = []
    for i in range(n):
        rot = ''
        for j in range(n):
            for k in range(n):
                if i == k:
                    rot += li[j][n - i - 1]
        return_list.append(rot)
    return return_list

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    base = [list(input().replace(' ', '')) for _ in range(N)]
    _90 = rotate(base, N)
    _180 = rotate(_90, N)
    _270 = rotate(_180, N)

    print(f'#{tc}')
    for t in list(zip(_270, _180, _90)):
        print(*t)