
# 해당 자릿수가 5보다 큰 경우, 5인 경우, 5보다 작은 경우 구분해서 생각.
# 굳굳
def solution(storey):
    answer = 0
    while storey != 0:
        n = storey % 10 
        if n >= 6:
            storey += 10 - n
            answer += 10 - n
        elif n == 5 and (storey // 10) % 10 >= 5:
            storey += 10 - n
            answer += 10 - n
        else:
            answer += n
        storey = storey // 10

    return answer