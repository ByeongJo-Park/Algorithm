import sys
input = sys.stdin.readline

N = int(input())

Lines = []

for _ in range(N):
    s, e = map(int, input().split())
    Lines.append([s, e])

Lines.sort()
ns, ne = Lines[0]
ans = 0
for __ in range(1, N):
    cs, ce = Lines[__]
    if ne > cs:
        ne = max(ne, ce)
    else:
        ans += (ne - ns)
        ns, ne = cs, ce

ans += (ne - ns)
print(ans)