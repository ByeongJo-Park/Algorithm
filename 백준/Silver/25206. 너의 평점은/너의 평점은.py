AP = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
AG = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
t = 0
k = 0

for i in range(20):
    a = list(map(str, input().split()))
    if a[2] in AG:
        t += float(a[1]) * AP[AG.index(a[2])]
        k += float(a[1])

print(t/k)