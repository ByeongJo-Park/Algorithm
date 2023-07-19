# N, M = map(int, input().split())
T = []
for t in range(1,31):
    T.append(0)

for i in range(0,28):
    a = int(input())
    T[a-1] = a

x = T.index(0)
y = T[::-1].index(0)

print(x + 1)
print(30 - y)