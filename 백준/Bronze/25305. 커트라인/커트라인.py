N, k = map(int,input().split())

x = list(map(int, input().split()))

x.sort()
t = x[::-1]

print(t[k-1])