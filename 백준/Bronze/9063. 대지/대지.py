N = int(input())
x = []
y = []
for i in range(0, N):
    a, b = map(int,input().split())
    x.append(a)
    y.append(b)

p = max(x) - min(x)
q = max(y) - min(y)

print(p * q)