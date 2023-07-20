T = int(input())

i = 0
k = 0
while True:
    k += i
    i += 1
    if k > T - 1:
        break

t = i - 1
 
tt = k - T

if t % 2 == 0:
    print(f'{t - tt}/{1 + tt}')
else:
    print(f'{1 + tt}/{t - tt}')