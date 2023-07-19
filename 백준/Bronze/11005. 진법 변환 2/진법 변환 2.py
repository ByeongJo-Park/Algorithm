import sys

t = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N, B = map(int, input().split())
A = ''
while N > (B-1):
    A += t[N % B]
    N = N // B
else:
    if N == 0:
        A = A[::-1]    
    else :
        A += t[N % B]
        A = A[::-1] 

print(A)