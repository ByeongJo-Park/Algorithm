

while True:
    x = list(map(int,input().split()))
    mx = max(x)
    sx = sum(x)
    dx = sx - mx
    if x[0] ==  x[1] == x[2] == 0:
        break
    else:
        if dx <= mx:
            print('Invalid')
            continue
        if x[0] ==  x[1] == x[2]:
            print('Equilateral')
        elif x[0] == x[1] or x[1] == x[2] or x[0] == x[2]:
            print('Isosceles')
        elif x[0] != x[1] != x[2]:
            print('Scalene')



