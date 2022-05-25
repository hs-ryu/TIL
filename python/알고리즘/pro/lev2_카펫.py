def solution(brown, yellow):
    flag = 0
    for i in range(3, brown):
        for j in range(3, brown):
            x = i * j
            y = (i-2) * (j-2)
            if x-y == brown and y == yellow:
                flag = 1
                answer = [j,i]
        if flag:
            break
            
    return answer