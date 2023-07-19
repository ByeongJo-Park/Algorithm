N = int(input())

d = ' '
k = '*'
for i in range(1, N + 1):
    print(((N-i) * d) + (i * k))