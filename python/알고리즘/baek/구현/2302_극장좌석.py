# 1 2 3 4 5 6 7 8 9 -> 가능
# 2 1 3 4 5 6 7 8 9 -> 가능
# 1 3 2 4 5 6 7 8 9 -> 가능
# 1 2 3 4 6 5 7 8 9 -> 가능
# 1 2 3 4 5 6 7 9 8 -> 가능
# 1 2 3 4 6 5 7 9 8 -> 가능

# 2 1 3 4 6 5 7 8 9 -> 가능
# 2 1 3 4 6 5 7 9 8 -> 가능
# 2 1 3 4 5 6 7 9 8 -> 가능

# 1 3 2 4 6 5 7 8 9 -> 가능
# 1 3 2 4 5 6 7 9 8 -> 가능
# 1 3 2 4 6 5 7 9 8 -> 가능

# 총 12
# 4 이전까지 가능한 경우의 수 -> 3
# 4 ~ 7 사이에 가능한 경우의 수 -> 2
# 7 이후 가능한 경우의 수 -> 2
# 3 * 2 * 2 => 12

# 일반 좌석 0개 -> 없음
# 일반 좌석 1개 -> 1가지
# 일반 좌석 2개 -> 2가지
# 일반 좌석 3개 -> 3가지
# 일반 좌석 4개 -> 5가지
# 1 2 3 4 
# 2 1 3 4
# 1 3 2 4
# 1 2 4 3
# 2 1 4 3
# 일반 좌석 5개 -> 8가지
# 1 2 3 4 5
# 2 1 3 4 5
# 1 3 2 4 5
# 1 2 4 3 5
# 1 2 3 5 4
# 2 1 4 3 5
# 2 1 3 5 4
# 1 3 2 5 4
# 일반 좌석 6개 -> 13가지?


n = int(input())
m = int(input())
cinema = [0] * (n+1)
for _ in range(m):
    k = int(input())
    cinema[k] = -1

# 일반 좌석 수에 따른 경우의 수를 넣을 리스트
calc_list = [0] * 41
calc_list[1] = 1
calc_list[2] = 2
for i in range(3,41):
    calc_list[i] = calc_list[i-2] + calc_list[i-1]

result_list = []
# vip 없을때
if m == 0:
    result = calc_list[n]
else:
    i = 1
    # vip 좌석 사이의 일반 좌석 수
    cnt = 0
    while i < n+1:
        # -1이면 vip좌석
        if cinema[i] == -1:
            result_list.append(calc_list[cnt])
            cnt = 0
        else:
            cnt += 1
        i += 1
    # 마지막 값 처리. (맨 마지막이 vip 좌석이 아니면 추가가 안되어 있을거니까)
    if cnt:
        result_list.append(calc_list[cnt])
    # print(cinema)
    # print(result_list)
    result = 1
    # 0도 추가되어있을거니까 0아닐때만 추가
    for i in range(len(result_list)):
        if result_list[i]:
            result *= result_list[i]
print(result)