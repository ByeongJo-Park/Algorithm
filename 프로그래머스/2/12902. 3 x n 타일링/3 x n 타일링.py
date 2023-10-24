mod = 1000000007

def solution(n):
    dp = [0] * (n+1)
    dp[0] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 2] * 3
        if i-4 >= 0 and i % 2 == 0:
            for j in range(i-4, -1, -2):
                dp[i] += dp[j]*2
    return dp[n]%mod