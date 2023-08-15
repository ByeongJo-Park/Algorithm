import sys
inp = sys.stdin.readline

T = int(inp())
St = [inp() for _ in range(T)]

St = list(set(St))
St.sort()
St.sort(key=len)

for k in St:
    k = k.replace('\n', '')
    print(k)