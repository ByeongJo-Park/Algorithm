c = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
t = []
for _ in range(3):
    t.append(input())

ans = (10 * c.index(t[0]) + c.index(t[1])) * (10**c.index(t[2]))
print(ans)