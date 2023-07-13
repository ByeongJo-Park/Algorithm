a, b = map(int, input().split())
# a = int(input())
# b = int(input())

if b >= 45 :
    a = a
    b = b - 45
else:
    if a == 0:
        a = 23
    else:
        a = a - 1
    
    b = b + 45 - 30


print(str(a) + " " + str(b))

