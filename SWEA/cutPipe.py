T = int(input())

for tc in range(1, T + 1):
    sit = input()
    stack = []
    l = len(sit)
    ans = 0
    for i in range(l):
        if sit[i] == '(':
            stack.append(sit[i])
        else:
            stack.pop()
            if sit[i-1] == '(':
                ans += len(stack)
            else:
                ans += 1
    print(f'#{tc} {ans}')