def fc(r, l):
    for i in range(1, l//2 + 1):
        if str(r)[l-i:] == str(r)[l-2*i:l-i]:
            return
    if l == N:
        print(r)
        exit(0)
    for i in range(1, 4):
        t = r * 10 + i
        fc(t, l+1)


N = int(input())
fc(0, 0)
