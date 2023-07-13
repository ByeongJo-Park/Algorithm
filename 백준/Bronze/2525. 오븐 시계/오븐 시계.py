a, b = map(int, input().split())
c = int(input())
# a = int(input())
# b = int(input())
f = c // 60
g = c % 60

if b + g >= 60:
    if a + f + 1>= 24:
        a = a + f - 23
        b = b + g - 60
    else:
        a = a + f + 1
        b = b + g - 60
else :
    if a + f >= 24:
        a = a + f - 24
        b = b + g
    else:
        a = a + f
        b = b + g





print(str(a) + " " + str(b))