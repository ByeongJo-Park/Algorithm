import sys
O = int(sys.stdin.readline())
stack = []
order_list = [list(map(int, sys.stdin.readline().split())) for _ in range(O)]
ans_list = []
for order in order_list:
    if order[0] == 1:
        stack.append(order[1])
    elif order[0] == 2:
        if len(stack) == 0:
            ans_list.append(-1)
        else:
            ans_list.append(stack.pop())
    elif order[0] == 3:
        ans_list.append(len(stack))
    elif order[0] == 4:
        if len(stack) == 0:
            ans_list.append(1)
        else:
            ans_list.append(0)
    else:
        if len(stack) == 0:
            ans_list.append(-1)
        else:
            ans_list.append(stack[-1])
for i in ans_list:
    print(i)