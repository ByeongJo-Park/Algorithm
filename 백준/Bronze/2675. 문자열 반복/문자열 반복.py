T = int(input())
r = ''
for i in range(T):
    A = list(map(str, input().split()))
    for k in A[1]:
        r += k * int(A[0])
    
    r += '\n'

print(r)
