N = int(input())
ans = 0
board = [0 for _ in range(N)]

def n_queen(n):
    global ans
    if n == N:
        ans += 1
        return
    else:
        for i in range(N):
            board[n] = i
            for i in range(n):
                if board[n] == board[i] or abs(board[n] - board[i]) == abs(n - i):
                    break
            else:
                n_queen(n+1)

n_queen(0)
print(ans)