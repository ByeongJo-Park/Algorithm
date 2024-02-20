N = int(input())
if N == 0:
    print(1)
else:
    ans = 1
    for t in range(1, N + 1):
        ans *= t
    print(ans)
