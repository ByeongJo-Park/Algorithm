T = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
W = input()
a = 0
for w in W:
    for t in T:
        if w in t:
            a += T.index(t) + 3

print(a)