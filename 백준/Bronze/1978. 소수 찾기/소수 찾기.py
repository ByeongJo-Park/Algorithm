T = int(input())

A = list(map(int, input().split()))
r = 0
for i in A:
    for j in range(1, i + 1):
        if j != 1 and j != i and i % j == 0:
            break
        if j == i:
            r += 1
    
if 1 in A:
    r -=1

print(r)