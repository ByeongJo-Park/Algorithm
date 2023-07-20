a = int(input())
b = int(input())
T = []
for i in range(a, b + 1):
    for j in range(1, i + 1):
        if j != 1 and j != i and i % j == 0:
            break
        if j == i:
            T.append(i)

if 1 in T:
    T.remove(1)

if len(T) == 0:
    print(-1)
else:
    print(sum(T))
    print(min(T))        
