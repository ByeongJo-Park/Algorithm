L =[]

for i in range(0, 9): 
    L.append(int(input()))

a = max(L)
b = L.index(a)
print(a)
print(b+1)

