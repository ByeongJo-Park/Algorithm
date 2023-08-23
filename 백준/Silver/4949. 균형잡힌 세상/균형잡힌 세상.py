import sys
inp = sys.stdin.readline

while True:
    s = inp().replace('\n', '')
    t = []
    ans = 'yes'
    if s == '.':
        break
    for i in s:
        if i in ['(', '[']:
            t.append(i)
        if i in [')', ']']:
            if len(t) == 0:
                ans = 'no'
                break
            else:
                a = t.pop()
                if (i == ')' and a != '(') or (i == ']' and a != '['):
                    ans = 'no'
                    break
        if i == '.':
            if len(t) > 0:
                ans = 'no'
                break
            else:
                break
    print(ans)
