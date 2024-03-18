def solution(n, computers):
    visited = [False] * n
    answer = 0
    for i in range(n):
        if visited[i] == False:
            dfs(n, computers, i, visited)
            answer += 1
    return answer


def dfs(n, computers, m, visited):
    visited[m] = True
    for k in range(n):
        if not visited[k] and computers[m][k] == 1:
            if not visited[k]:
                dfs(n, computers, k, visited)