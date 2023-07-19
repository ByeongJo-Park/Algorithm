import sys

t = True

while t == True:
    try:
        a , b = map(int, sys.stdin.readline().split())
        print(a + b)
    except:
        break
    