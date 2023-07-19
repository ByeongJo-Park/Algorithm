T = int(input())
A = 2 * T - 1

for i in range(1, A + 1):
    if i < T + 1:
        r = ' ' * (T-i) + '*' * (2 * i -1)
        print(r)
    else:
        r = ' ' * (i - T) + '*' * (2 * (A + 1 - i) - 1)
        print(r)
