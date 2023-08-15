import sys
from copy import deepcopy
inp = sys.stdin.readline

N, M = map(int, inp().split())
pl = {inp().replace('\n', '') : str(1 + _) for _ in range(N)}
rpl = {v : k for k, v in pl.items()}
ol = [inp().replace('\n', '') for _ in range(M)]

for o in ol:
    if o.isdigit():
        print(rpl[o])
    else:
        print(pl[o])