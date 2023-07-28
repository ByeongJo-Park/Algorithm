import sys
t = int(input())
ans = []

def pacto(num):
    t = 1
    for i in range(1, num + 1):
        t *= i
    return t 

for i in range(t):
    N, M = map(int, sys.stdin.readline().split())
    print(pacto(M)//(pacto(M-N)*pacto(N)))
