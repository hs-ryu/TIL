# 큰수, 작은수

# 문자 -> 숫자로 바꾸기
# 10의 (문자열 길이 - 1) 제곱
# 마지막에 K 붙어 있으면 5 곱해주기.
def change(s):
    
    result = 10 ** (len(s) - 1)
    if s[-1] == 'K':
        result *= 5
    return str(result)

# 최소의 경우 M/K/K/MM/K => K가 나오면, K 이전까지 나온 문자열 더해줌.
# K는 따로 더해준다.
def MIN():
    answer = ''
    st = ''
    i = 0
    while i < len(string):
        # print(answer)
        if string[i] == 'K':
            if st:
                answer += change(st)
                answer += change('K')
            else:
                answer += change('K')
            st = ''
        else:
            st += 'M'
        i += 1
    if st:
        answer += change(st)
    # print(answer)
    return answer

# 최대의 경우 MK/K/MMK/M/M => K 만나면 이전까지 문자열에 K 더해줘서 변환.
# 마지막이 K로 안끝나면, MM(10) 이 아니라 M/M (11) 으로 따로따로 봐야함
def MAX():
    answer = ''
    st = ''
    i = 0
    while i < len(string):
        if string[i] == 'K':
            st += 'K'
            answer += change(st)
            st = ''
        else:
            st += 'M'
        i += 1
    if (st):
        answer += '1' * len(st)
    return answer


string = input()
result1 = MIN()
result2 = MAX()
print(result2)
print(result1)