def solution(A, B):
    answer = 0
    lena = len(A)
    A.sort(reverse=True)
    B.sort(reverse=True)
    k = 0
    for i in range(lena):
        if (A[i] < B[k]):
            answer += 1
            k += 1
    return answer