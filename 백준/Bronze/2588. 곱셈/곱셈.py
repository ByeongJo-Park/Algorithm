a = int(input())
b = int(input())
c = list(map(int, str(b)))

d = c[0] * a
e = c[1] * a
f = c[2] * a

print(f)
print(e)
print(d)
print(100 * d + 10 * e + f)