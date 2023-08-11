import sys
inp = sys.stdin.readline
dp = [1, 3]

N = int(inp())

while len(dp) < N:
    k = len(dp)
    dp.append(dp[k-1] + (2 * dp[k-2]))

print(dp[N-1] % 10007)