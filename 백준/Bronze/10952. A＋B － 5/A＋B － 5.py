import sys

t = True

while t == True:
    a , b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0:
        t = False
    else:
        print(a + b)
    
