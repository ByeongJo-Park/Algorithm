S = input().upper()
T ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
C = []

for t in T:
    C.append(S.count(t))

if C.count(max(C)) > 1:
    print('?')
else:
    print(T[C.index(max(C))])

        