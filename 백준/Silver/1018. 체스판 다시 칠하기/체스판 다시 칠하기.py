n, m = map(int, input().split())
p = []
ans = []

for t in range(n):
    p.append(input())

for i in range(n-7):
    for j in range(m-7):
        d1 = 0
        d2 = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:
                    if p[a][b] != 'W':
                        d1 += 1
                    if p[a][b] != 'B':
                        d2 += 1
                else:
                    if p[a][b] != 'B':
                        d1 += 1
                    if p[a][b] != 'W':
                        d2 += 1

        ans.extend([d1, d2])
print(min(ans))