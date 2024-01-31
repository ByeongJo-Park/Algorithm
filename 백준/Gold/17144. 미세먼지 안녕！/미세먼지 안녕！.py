import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())

house, air_cleaner = [], []
# 상하좌우(확산)
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# 위쪽 공기청정기 우, 상, 좌, 하
up_dir = [[0, 1], [-1, 0], [0, -1], [1, 0]]
# 아래쪽 공기청정기 우, 하, 좌, 상
down_dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# house 채우기
for _ in range(r):
    house.append(list(map(int, input().split())))
    for __ in range(c):
        if house[_][__] == -1:
            air_cleaner.append([_, __])

# 확산함수
def dust():
    # 확산 계산
    dusts = [[0 for _ in range(c)] for __ in range(r)]
    for i in range(r):
        for j in range(c):
            if not (house[i][j] == 0 or house[i][j] == -1):
                # 확산 방향수
                direction = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < r and 0 <= nj < c and [ni, nj] not in air_cleaner:
                        direction += 1
                        dusts[ni][nj] += house[i][j] // 5
                house[i][j] = house[i][j] - (house[i][j] // 5 * direction)

    # 현재 집 먼지계산
    for i in range(r):
        for j in range(c):
            house[i][j] += dusts[i][j]

    return

def air_clean(air):
    for i, j in air:
        turning = 0
        si, sj = i, 1
        tmp = 0
        while True:
            dirs = []
            if [i, j] == air[0]:
                dirs = up_dir
            else:
                dirs = down_dir
            ni, nj = si + dirs[turning][0], sj + dirs[turning][1]
            if si == i and sj == 0:
                break

            if ni < 0 or ni >= r or nj < 0 or nj >= c:
                turning += 1
                continue

            house[si][sj], tmp = tmp, house[si][sj]

            si, sj = ni, nj
    return

for _ in range(t):
    dust()
    air_clean(air_cleaner)

ans = 0
for i in range(r):
    for j in range(c):
        if house[i][j] > 0:
            ans += house[i][j]

print(ans)