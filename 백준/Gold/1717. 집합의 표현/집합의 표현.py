import sys
inp = sys.stdin.readline

def find_set(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find_set(parent[x])
        return parent[x]

def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if px != py:
        parent[px] = py

N, M = map(int, inp().rstrip().split())

parent = [i for i in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, inp().rstrip().split())
    
    if a == 0:
        if b != c:
            union(b, c)
    else:
        if b != c:
            if find_set(b) == find_set(c):
                print('YES')
            else:
                print('NO')
        else:
            print('YES')