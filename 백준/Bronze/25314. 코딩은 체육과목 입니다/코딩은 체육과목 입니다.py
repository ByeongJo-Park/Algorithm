N = int(input())

t = N // 4
ans = ''
while t >= 1:
    ans += 'long '
    t -= 1
else:
    ans += 'int'

print(ans)