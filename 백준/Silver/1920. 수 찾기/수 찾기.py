N = int(input())
n = set(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))

for i in m:
    print(1) if i in n else print(0)