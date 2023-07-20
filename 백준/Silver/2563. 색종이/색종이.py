S = [[0] * 101 for i in range(101)]

T = int(input())
last = 0

for t in range(T):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            S[i+a][j+b] = 1


for k in S:
    last += sum(k)

print(last)
