# 시분초를 변수로 입력하고 나서 1001초 후의 시간을 출력해주세요!
# 24시간이 넘는 경우에는 0으로 초기화 합니다

# 아래의 변수 할당 값은 바뀔 수 있음!
# hour = 23
# min = 59
# second = 40

# 1001초 후의 시간으로 변경
# print(hour, min, second) 

int_hour = int(input('Hour? : '))
int_min = int(input('Min? : '))
int_sec = int(input('Seconds? : '))
int_plus_sec = 1001 % 60
int_plus_min = 1001 // 60
int_plus_hour = 0

int_ans_hour = 0
int_ans_min = 0
int_ans_sec = 0

# 입력 제한
if int_hour > 23 :
    print('24시를 초과했습니다.')
    int_min = int(input('Hour? : '))

if int_min > 59:
    print('60분을 초과했습니다.')
    int_min = int(input('Min? : '))

if int_sec > 59:
    print('60초을 초과했습니다.')
    int_sec = int(input('Seconds? : '))

# 초 계산
if int_sec + int_plus_sec > 60:
    int_ans_sec = int_sec + int_plus_sec - 60
    int_plus_min += 1
else:
    int_ans_sec = int_sec + int_plus_sec

# 분 계산
if int_min + int_plus_min > 60:
    int_ans_min = int_min + int_plus_min - 60
    int_plus_hour += 1
else:
    int_ans_min = int_min + int_plus_min

# 시간 계산
if int_hour + int_plus_hour > 23:
    int_ans_hour = int_hour + int_plus_hour - 24
else:
    int_ans_hour = int_hour + int_plus_hour

# 출력
print(int_ans_hour, int_ans_min, int_ans_sec)
print(str(int_ans_hour) + ':' + str(int_ans_min) + ':' + str(int_ans_sec))

totalseconds = (int_hour * 60 * 60) + (int_min * 60) + int_sec + 1001
final_hour = totalseconds // 3600 % 24 
final_min = totalseconds % 3600 // 60
final_sec = totalseconds % 60

print(final_hour, final_min, final_sec)