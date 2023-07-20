TC = int(input())
a = 0
for tc in range(TC):
    Txts = input()
    
    A = []
    for i in range(len(Txts)):
        if i == 0:
            A.append(Txts[i])
        else:
            if Txts[i] == Txts[i-1]:
                continue
            else:
                A.append(Txts[i])
    
    if len(A) == len(list(set(A))):
        a += 1

print(a)    