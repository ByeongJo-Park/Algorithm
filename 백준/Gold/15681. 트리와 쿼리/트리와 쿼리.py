import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
# 입력
N, R, Q = map(int, input().split())

# 트리 정보
TreeInfo = [[] for _ in range(N+1)]

# 출력할 쿼리들 배열
query = []

visit = [0 for _ in range(N+1)]
# 트리 정보 담기
for _ in range(N-1):
    U, V = map(int, input().split())
    TreeInfo[U].append(V)
    TreeInfo[V].append(U)

# 쿼리 순서대로 담기
for _ in range(Q):
    query.append(int(input()))

# DFS
def DFS(S):
    # 루트 최소 1확보
    visit[S] = 1
    for i in TreeInfo[S]:
        # 0? DFS 타라
        if not visit[i]:
            DFS(i)
            visit[S] += visit[i]

DFS(R)

for q in query:
    print(visit[q])