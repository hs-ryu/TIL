N = int(input())
numbers = [1] * 1000
# 경우의 수 줄이기.
for i in range(123, 1000):
    str_i = str(i)
    if str_i[0] == str_i[1] or str_i[0] == str_i[2] or str_i[1] == str_i[2]:
        numbers[i] = 0
    if str_i[0] == '0' or str_i[1] == '0' or str_i[2] == '0':
        numbers[i] = 0


for _ in range(N):
    num, strike, ball = input().split()
    # 123~987까지 하나씩 비교
    for number in range(123, 1000):
        compare_num = str(number)
        strikecnt = 0
        ballcnt = 0
        if numbers[number]:
        # 입력받은 num에서 한 자리씩 비교
            for i in range(3):
                # 123~987 중 한 숫자에서 한 자리씩 가져와서 num의 자리값과 비교
                for j in range(3):
                    if i == j and num[i] == compare_num[j]:
                        strikecnt += 1
                    elif i != j and num[i] == compare_num[j]:
                        ballcnt += 1
            if strikecnt != int(strike) or ballcnt != int(ball):
                numbers[number] = 0

print(numbers[123:1000].count(1))
