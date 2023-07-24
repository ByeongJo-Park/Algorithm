n = int(input())

a = n // 3
b = n // 5
c = True

if a == 0 and b == 0:
    print(-1)

for i in range(0,a+1):
    for j in range(0, b+1):
        if (5 * j) + (3 * i) == n:
            print(j + i)
            c = False
            break
        if i == a and j == b:
            print(-1)
    if c == False:
        break