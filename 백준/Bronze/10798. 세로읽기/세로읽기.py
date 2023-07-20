a = []
b = []
c = 0
for i in range(5):
    a.append(input())
    b.append(len(a[i]))

c = max(b)
d = ''

for j in range(5):
    if len(a[j]) == c:
        continue
    else:
        a[j] += ' ' * (c - len(a[j]))

for k in range(c):
    for t in range(5):
        d += a[t][k]
    

print(d.replace(' ', ''))