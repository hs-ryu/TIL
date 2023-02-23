def solution(food):
    answer = ''
    
    temp = []
    for i in range(1,len(food)):
        temp += str(i) * (food[i] // 2)
    answer += "".join(temp)
    answer += "0"
    answer += "".join(reversed(temp))
    
    return answer