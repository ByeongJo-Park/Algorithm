T = int(input())

for i in range(T):
    p = []
    m = int(input())
    p.append(m//25)
    m = m % 25
    p.append(m//10)
    m = m % 10
    p.append(m//5)
    m = m % 5
    p.append(m)
    print(*p)