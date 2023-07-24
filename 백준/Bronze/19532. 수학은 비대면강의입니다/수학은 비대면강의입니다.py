a,b,c,d,e,f = map(int, input().split())
h = True
for i in range(-999, 1000):
    for j in range(-999, 1000):
        if a*i + b*j ==c and d*i + e*j == f:
            print(i,j)
            h = False
            break
        if not h:
            break    
    if not h:
        break