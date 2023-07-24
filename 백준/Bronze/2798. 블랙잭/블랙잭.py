n, m = map(int, input().split())
a = list(map(int, input().split()))
b = []
a.sort()
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and i != k and j != k:
                if a[i] + a[j] + a[k] <= m:
                    b.append(a[i] + a[j] + a[k])

print(max(b))