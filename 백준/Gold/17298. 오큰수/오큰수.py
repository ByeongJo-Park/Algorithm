import sys
input = sys.stdin.readline

N = int(input())
first = list(map(int, input().split()))
ans = [-1] * N
st = [0]
# for 문을 돌면서 스택에 있는걸로 비교하면서 갱신해줌
for i in range(1, N):
    while st and first[st[-1]] < first[i]:
        ans[st.pop()] = first[i]
    st.append(i)

print(*ans)
