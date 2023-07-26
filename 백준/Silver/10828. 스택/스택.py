import sys
t = int(sys.stdin.readline())
ol = []
b =[]
for i in range(t):
    a = sys.stdin.readline()
    if 'push' in a:
        b = list(a.split())
        ol.append(int(b[1]))
    elif 'pop' in a:
        if len(ol) == 0:
            print(-1)
        else:
            print(ol.pop())
    elif 'size' in a:
        print(len(ol))
    elif 'empty' in a:
        if len(ol) == 0:
            print(1)
        else:
            print(0)
    elif 'top' in a:
        if len(ol) == 0:
            print(-1)
        else:
            print(ol[-1])

