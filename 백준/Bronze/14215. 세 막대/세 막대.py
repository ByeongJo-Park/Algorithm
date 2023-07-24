a = list(map(int, input().split()))

b = max(a)

c = sum(a)

d = c - b

if d <= b:
    a[a.index(b)] = d - 1

print(sum(a))