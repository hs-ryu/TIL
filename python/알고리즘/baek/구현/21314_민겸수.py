# 큰수, 작은수

def change(s):
    
    result = 10 ** (len(s) - 1)
    if s[-1] == 'K':
        result *= 5
    return str(result)



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