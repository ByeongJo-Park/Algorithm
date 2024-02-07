N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

ans = 0
for i in range(N):
    A[i] = max(A[i] - B, 0)
    ans += 1

for i in range(N):
    r, c = A[i] // C, A[i] % C
    if c > 0:
        ans += r + 1
    else:
        ans += r

print(ans)
