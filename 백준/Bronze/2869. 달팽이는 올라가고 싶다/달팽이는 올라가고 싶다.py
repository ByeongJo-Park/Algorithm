A, B, V = map(int, input().split())

k = (V - A) / (A - B)

if k == int(k) :
    print(int(k) + 1)
else:
    print(int(k) + 2)
