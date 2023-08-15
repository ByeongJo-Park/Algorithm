import sys
from copy import deepcopy
inp = sys.stdin.readline

S = inp().replace('\n', '')
K = len(S)
n = set()
for i in range(K):
    for j in range(K-i):
        n.add(S[j:j+i+1])

print(len(n))