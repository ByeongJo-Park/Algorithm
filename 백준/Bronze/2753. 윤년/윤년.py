# a, b = map(int, input().split())
a = int(input())
b = 0

if a % 4 == 0:
    if a % 100 == 0:
        if a % 400 == 0:
            b = 1
        else :
            b = 0
    else:
        b = 1
else:
    b = 0

print(b)

