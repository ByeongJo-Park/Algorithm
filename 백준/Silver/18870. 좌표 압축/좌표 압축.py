import sys
from copy import deepcopy
inp = sys.stdin.readline

T = int(inp())

St = list(map(int, inp().split()))
Co_St = deepcopy(St)
St = list(sorted(set(St)))
dic = {St[i] : i for i in range(len(St))}

for i in range(T):
    print(dic[Co_St[i]], end= ' ')