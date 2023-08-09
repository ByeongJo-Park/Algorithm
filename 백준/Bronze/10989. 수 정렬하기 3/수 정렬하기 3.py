import sys

N = int(sys.stdin.readline())
count_list = [0] * 100001

for i in range(N):
    count_list[int(sys.stdin.readline())] += 1

j = 0
while N > 0:
    if count_list[j] == 0:
        j += 1
    else:
        N -= 1
        count_list[j] -= 1
        print(j)
