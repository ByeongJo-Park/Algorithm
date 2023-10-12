# 11279 : 최대 힙
import heapq
import sys
input = sys.stdin.readline

# n
n = int(input().strip())
arr = []
for _ in range(n):
    num = - int(input().strip())
    if num == 0:
        if not arr:
            print(0)
        else:
            print(-heapq.heappop(arr))
    else:
        heapq.heappush(arr, num)