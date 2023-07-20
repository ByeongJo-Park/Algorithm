while True:
    n = int(input())
    t = []
    if n == -1:
        break

    for i in range(1, n + 1):
        if n % i == 0:
            t.append(i)

    if (sum(t) - n) == n:
        print(f'{n} =', end=' ')
        for j in range(len(t)-1):
            if j != (len(t) - 2):
                print(f'{t[j]} + ', end = '')
            else:
                print(f'{t[j]}')

    else:
        print(f'{n} is NOT perfect.')