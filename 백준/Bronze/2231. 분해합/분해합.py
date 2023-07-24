a = int(input())

for i in range(a+1):
    gen = i
    gensum = sum(map(int,str(i)))
    check = gen + gensum
    if check == a:
        print(gen)
        break
    if i == a:
        print(0)