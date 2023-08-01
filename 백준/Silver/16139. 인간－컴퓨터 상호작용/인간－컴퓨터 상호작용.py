import sys

Case_str = sys.stdin.readline()
N = int(sys.stdin.readline())
for i in range(N):
    case = list(map(str, sys.stdin.readline().split()))
    check_str = Case_str[int(case[1]):int(case[2])+1]
    print(check_str.count(case[0]))    