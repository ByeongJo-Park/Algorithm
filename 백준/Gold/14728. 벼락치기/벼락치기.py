import sys

N, T = map(int, input().split())
DP = [0] * (T+1)
for _ in range(N):
    K, S = map(int, input().split())
    for i in range(T, -1, -1):
        if i >= K:
            DP[i] = max(DP[i], DP[i-K] + S)
print(DP[T])