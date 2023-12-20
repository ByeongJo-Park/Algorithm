import sys

from itertools import permutations

input = sys.stdin.readline

# 이닝수
N = int(input())

# 각 이닝별 정보
innings_info = [list(map(int, input().split())) for _ in range(N)]

# 4번타자를 제외한 타순을 위한 리스트
hitter_list = [1, 2, 3, 4, 5, 6, 7, 8]

# 갱신할 answer 최대값 찾기 위한 0부터
answer = 0

# 순열 + 4번 타자 부터 시작
for perm in permutations(hitter_list):
    p = list(perm)
    hitter_order = p[:3] + [0] + p[3:]
    score = 0
    current = 0
    for inning in range(N):
        out_cnt = 0
        # 베이스 정보
        b_1, b_2, b_3 = 0, 0, 0

        while out_cnt < 3:
            hit_type = innings_info[inning][hitter_order[current]]
            if hit_type == 0:
                out_cnt += 1
            elif hit_type == 1:
                score += b_3
                b_1, b_2, b_3 = 1, b_1, b_2
            elif hit_type == 2:
                score += b_2 + b_3
                b_1, b_2, b_3 = 0, 1, b_1
            elif hit_type == 3:
                score += b_1 + b_2 + b_3
                b_1, b_2, b_3 = 0, 0, 1
            elif hit_type == 4:
                score += b_1 + b_2 + b_3 + 1
                b_1, b_2, b_3 = 0, 0, 0

            current = (current + 1) % 9

    if answer <= score:
        answer = score

print(answer)