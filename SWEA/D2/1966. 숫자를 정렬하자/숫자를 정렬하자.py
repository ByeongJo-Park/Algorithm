T = int(input())

for i in range(1, 1 + T):

    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(f'#{i}', end=' ')
    print(*a)