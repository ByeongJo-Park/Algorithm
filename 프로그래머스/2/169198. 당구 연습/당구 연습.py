def solution(m, n, startX, startY, balls):
    answer = []
    for x,y in balls:
        if startY != y and startX != x:
            a = (abs(startX-(-x))**2) + (abs(startY-y)**2)
            b = (abs(startX-x)**2) + (abs(startY-(-y))**2)
            c = (abs(startX-(2*m-x))**2) + (abs(startY-y)**2)
            d = (abs(startX-x)**2) + (abs(startY-(2*n-y))**2)
        elif startY == y:
            a = (abs(startX-(-x))**2) + (abs(startY-y)**2) if startX < x else 10000000
            b = (abs(startX-x)**2) + (abs(startY-(-y))**2)
            c = (abs(startX-(2*m-x))**2) + (abs(startY-y)**2)  if startX > x else 10000000
            d = (abs(startX-x)**2) + (abs(startY-(2*n-y))**2)
        elif startX == x:
            a = (abs(startX-(-x))**2) + (abs(startY-y)**2)
            b = (abs(startX-x)**2) + (abs(startY-(-y))**2) if startY < y else 10000000
            c = (abs(startX-(2*m-x))**2) + (abs(startY-y)**2)
            d = (abs(startX-x)**2) + (abs(startY-(2*n-y))**2) if startY > y else 10000000
        answer.append(min(a, b, c, d))
    return answer