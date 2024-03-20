from collections import deque as q

def solution(begin, target, words):
    answer = 0

    if target not in words:
        return answer

    def bfs(now, depth):
        que = q([])
        que.append([now, depth])
        while que:
            n, d = que.popleft()
            for word in words:
                count = 0
                for i in range(len(word)):
                    if n[i] != word[i]:
                        count += 1
                if count == 1:
                    que.append([word, d + 1])
                if n == target:
                    return d

    return bfs(begin, 0)