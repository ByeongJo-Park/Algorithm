from collections import deque

def solution(n, edge):
    answer = 0
    roots = [[] for _ in range(n+1)]
    dists = [-1 for _ in range(n+1)]


    for info in edge:
        i, o = info
        roots[i].append(o)
        roots[o].append(i)

    q = deque()
    q.append(1)
    
    dists[1] = 0
    
    while q:
        node = q.popleft()
        for now in roots[node]:
            if dists[now] == -1:
                q.append(now)
                dists[now] = 1 + dists[node]
    answer = dists.count(max(dists))

    return answer
