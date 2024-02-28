from itertools import combinations

N = int(input())

ans = []

for i in range(1, 11):
    for j in combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], i):
        ans.append(int(''.join(list(map(str, reversed(list(j)))))))

ans.sort()

if N >= len(ans):
    print(-1)
else:
    print(ans[N])