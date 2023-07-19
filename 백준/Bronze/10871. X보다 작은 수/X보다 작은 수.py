N = list(map(int, input().split()))

L = list(map(int, input().split()))

C = []
for i in L:
    if i < N[1]:
        C.append(i)

print(*C)