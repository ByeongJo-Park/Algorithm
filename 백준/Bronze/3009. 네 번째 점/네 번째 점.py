a1, b1= map(int,input().split())
a2, b2= map(int,input().split())
a3, b3= map(int,input().split())
a4, b4 = 0, 0

a = [a1, a2, a3, a4]
b = [b1, b2, b3, b4]

for i in range(0,3):
    if a.count(a[i]) == 1:
        a4 = a[i]
    if b.count(b[i]) == 1:
        b4 = b[i]

print(a4, b4)