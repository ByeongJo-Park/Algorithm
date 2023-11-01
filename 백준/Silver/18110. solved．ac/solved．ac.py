import sys

input = sys.stdin.readline

N = int(input())
T = 0
if N == 0:
    print(0)
elif N <= 3:
    for _ in range(N):
        T += int(input())
        print(int((T/N) + 0.5))
else:
    nums = []
    out = int(N * 0.15 + 0.5)

    for _ in range(N):
        nums.append(int(input()))
    nums.sort()
    ans = nums[out:N-out]
    
    print(int((sum(ans) / (N - (2 * out))) + 0.5))
