A = list(map(int, input().split()))
A.sort()

if A[0] != A[1] != A[2]:
    print(A[2] * 100)
elif A[0] == A[1] != A[2]:
    print((A[1] * 100) + 1000)
elif A[1] == A[2] != A[0]:
    print((A[1] * 100) + 1000)
elif A[0] == A[2]:
    print((A[2] * 1000) + 10000)