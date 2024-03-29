def solution(triangle):
    lt = len(triangle)
    answer = [[0 for _ in range(i + 1)] for i in range(lt)]
    answer[0] = triangle[0]
    for i in range(lt-1):
        for j in range(len(answer[i])):
            for k in range(j, j+2):
                answer[i+1][k] = max(answer[i+1][k], answer[i][j] + triangle[i+1][k])

    # return answer
    return max(answer[-1])