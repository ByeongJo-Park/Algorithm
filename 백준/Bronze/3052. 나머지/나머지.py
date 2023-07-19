# N, M = map(int, input().split())
T = []
for t in range(1,11):
    T.append(int(input()))

for l in range(0, 10):
    T[l] = T[l] % 42

K = set(T)

print(len(K))