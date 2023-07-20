a, b = map(int, input().split())
t=[]
for i in range(0, a * 2):
    t.append(list(map(int,input().split())))

s =[]
for j in range(0, a):
    s.append([])
    for k in range(0, b):
        s[j].append(t[j][k] + t[j + a][k])

for al in s:
    print(*al)