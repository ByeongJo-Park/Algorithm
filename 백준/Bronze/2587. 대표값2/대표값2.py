b= []
for i in range(5):
    a = int(input())
    b.append(a)

b.sort()

print(sum(b)//5)

print(b[2])

