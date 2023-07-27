import sys
T = int(sys.stdin.readline())

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    ad = a % 10
    
    return_list = [10, 1,2,3,4,5,6,7,8,9]
    if ad == 0 :
        print(return_list[0])
    elif ad == 1:
        print(return_list[1])
    elif ad == 2:
        bd = b % 4
        if bd == 0:
            print(return_list[6])
        elif bd == 1:
            print(return_list[2])
        elif bd == 2:
            print(return_list[4])
        elif bd == 3:
            print(return_list[8])
    elif ad == 3:
        bd = b % 4
        if bd == 0:
            print(return_list[1])
        elif bd == 1:
            print(return_list[3])
        elif bd == 2:
            print(return_list[9])
        elif bd == 3:
            print(return_list[7])
    elif ad == 4:
        bd = b % 2
        if bd == 0:
            print(return_list[6])
        elif bd == 1:
            print(return_list[4])
    elif ad == 5:
        print(return_list[5])
    elif ad == 6:
        print(return_list[6])
    elif ad == 7:
        bd = b % 4
        if bd == 0:
            print(return_list[1])
        elif bd == 1:
            print(return_list[7])
        elif bd == 2:
            print(return_list[9])
        elif bd == 3:
            print(return_list[3])
    elif ad == 8:
        bd = b % 4
        if bd == 0:
            print(return_list[6])
        elif bd == 1:
            print(return_list[8])
        elif bd == 2:
            print(return_list[4])
        elif bd == 3:
            print(return_list[2])
    elif ad == 9:
        bd = b % 2
        if bd == 0:
            print(return_list[1])
        elif bd == 1:
            print(return_list[9])                             