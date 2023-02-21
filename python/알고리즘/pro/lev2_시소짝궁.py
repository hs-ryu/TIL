# 시간초과
def solution(weights):
    answer = 0
    
    for i in range(len(weights)-1):
        one = weights[i]
        for j in range(i+1,len(weights)):
            two = weights[j]
            
            one_list = [one, one*2, one*3, one*4]
            two_list = [two, two*2, two*3, two*4]
            for k in range(4):
                if two_list[k] in one_list:
                    answer += 1
                    break

    return answer

# 딕셔너리 이용해서 풀기
def solution(weights):
    answer = 0
    answerdiv2 = 0
    dic = {}

    for i in weights:
        dic[i] = dic.get(i, 0)
        dic[i] += 1


    for i in dic:
        x2 = i * 2
        if(x2 % 3 == 0):
            if(int(x2 / 3) in dic):
                answerdiv2 += int(dic[i] * dic[x2 / 3])
        if(x2 % 4 == 0):
            if(int(x2 / 4) in dic):
                answerdiv2 += int(dic[i] * dic[x2 / 4])

        x3 = i * 3
        if(x3 % 2 == 0):
            if(int(x3 / 2) in dic):
                answerdiv2 += int(dic[i] * dic[x3 / 2])
        if(x3 % 4 == 0):
            if(int(x3 / 4) in dic):
                answerdiv2 += int(dic[i] * dic[x3 / 4])

        x4 = i * 4
        if(x4 % 2 == 0):
            if(int(x4 / 2) in dic):
                answerdiv2 += int(dic[i] * dic[x4 / 2])
        if(x4 % 3 == 0):
            if(int(x4 / 3) in dic):
                answerdiv2 += int(dic[i] * dic[x4 / 3])

        answer += int(dic[i] * (dic[i] - 1) / 2)

    answer += int(answerdiv2/2)


    return answer