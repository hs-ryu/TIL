def solution(name, yearning, photo):
    answer = []
    # very easy. 딕셔너리에 다 때려박고 계산해준다.
    points = dict()
    for i in range(len(name)):
        points[name[i]] = yearning[i]
    for p in photo:
        result = 0
        for n in p:
            if n in points:
                result += points[n]
        answer.append(result)
    
    return answer