# 2 <= N <= 100
N = int(input())
# 성냥 DP 배열
matches = [[0, 0] for _ in range(101)]

# 규칙 찾기
# 성냥 개수
# N = 0 일 때, max = 0, min = 0
# N = 1 일 때, max = 0, min = 0
# N = 2 일 때, max = 1, min = 1 2
# N = 3 일 때, max = 7, min = 7 3
# N = 4 일 때, max = 11, min = 4 4
# N = 5 일 때, max = 71, min = 2 5
# N = 6 일 때, max = 111, min = 6 6
# N = 7 일 때, max = 711, min = 8 7
# N = 8 일 때, max = 1111, min = 10 2+6
# N = 9 일 때, max = 7111, min = 18 2+7
# N = 10 일 때, max = 11111, min = 22 5+5
# N = 11 일 때, max = 71111, min = 20 5+6
# N = 12 일 때, max = 111111, min = 28 5+7
# N = 13 일 때, max = 711111, min = 68 6+7
# N = 14 일 때, max = 1111111, min = 88 7+7
# N = 15 일 때, max = 7111111, min = 108 2+6+7
# N = 16 일 때, max = 11111111, min = 188 2+7+7
# N = 17 일 때, max = 71111111, min = 200 5+6+6
# N = 18 일 때, max = 111111111, min = 208 5+6+7
# N = 19 일 때, max = 711111111, min = 288 5+7+7
# N = 20 일 때, max = 1111111111, min = 688 6+7+7
# N = 21 일 때, max = 7111111111, min = 888 7+7+7
# N = 22 일 때, max = 11111111111, min = 1088 2+6+7+7
# N = 23 일 때, max = 71111111111, min = 1888 2+7+7+7
# N = 24 일 때, max = 111111111111, min = 2008 5+6+6+7
# 최대값
# N 이 짝수 일때, N//2자리 만큼 1이 최대이고 홀수 일때, N//2자리 만큼 1로 채우고 제일 앞자리를 7로 바꿈.
matches[2][0] = '1'
matches[2][1] = '1'
matches[3][0] = '7'
matches[3][1] = '7'
matches[4][0] = '11'
matches[4][1] = '4'
matches[5][0] = '71'
matches[5][1] = '2'
matches[6][0] = '111'
matches[6][1] = '6'
matches[7][0] = '711'
matches[7][1] = '8'
matches[8][0] = '1111'
matches[8][1] = '10'
matches[9][0] = '7111'
matches[9][1] = '18'
matches[10][0] = '11111'
matches[10][1] = '22'
matches[11][0] = '71111'
matches[11][1] = '20'
for i in range(12, 101):
    if i % 2 == 0:
        matches[i][0] = '1' * (i // 2)
    else:
        matches[i][0] = '7' + '1' * (i // 2 - 1)

    if i == 17:
        matches[i][1] = '200'
    else:
        matches[i][1] = matches[i-7][1] + '8'

for i in range(N):
    k = int(input())
    print(matches[k][1], matches[k][0])