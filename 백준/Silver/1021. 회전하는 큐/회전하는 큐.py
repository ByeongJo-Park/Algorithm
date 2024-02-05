from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
target = list(map(int, input().split()))
q = deque([i for i in range(1, n+1)])

ans = 0
for t in target:
    while True:
        if q[0] == t:
            q.popleft()
            break
        else:
            if q.index(t) < len(q)/2:
                while q[0] != t:
                    q.append(q.popleft())
                    ans += 1
            else:
                while q[0] != t:
                    q.appendleft(q.pop())
                    ans += 1
print(ans)