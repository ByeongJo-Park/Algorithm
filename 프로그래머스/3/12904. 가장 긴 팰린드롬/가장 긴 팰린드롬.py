def solution(s):
    answer = 1
    ls = len(s)
    for i in range(ls):
        for j in range(ls, i, -1):
            check = s[i:j]
            revers_check = check[::-1]
            if check == revers_check:
                answer = max(answer, j-i)
    return answer