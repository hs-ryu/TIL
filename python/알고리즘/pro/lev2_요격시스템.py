def solution(targets):
    answer = 1
    targets.sort(key=lambda x:x[0])
    temp_line = targets[0][1] - 0.5
    # 3
    for target in targets[1:]:
        # 선을 긋고, 다음 것을 확인한다.
        if temp_line < target[0]:
            answer += 1
            temp_line = target[1] - 0.5
        # 선 위치를 재조정 한다. 현재 선과, 현재 범위를 보는데 현재 범위가 더 작다면 그 쪽으로 선위치를 맞춰줘야 범용성이 좋다.
        else:
            temp_line = min(temp_line, target[1] - 0.5)
    
    
    
    
    return answer