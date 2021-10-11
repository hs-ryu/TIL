# 2개 중 긴걸 가로로 몰자.

def solution(sizes):
    max_width = 0
    max_height = 0
    
    for i in range(len(sizes)):
        # 가로가 더 크면 그냥 생각
        if sizes[i][0] > sizes[i][1]:
            if sizes[i][0] > max_width:
                max_width = sizes[i][0]
            if sizes[i][1] > max_height:
                max_height = sizes[i][1]
        # 세로가 더 크면 돌려서 생각
        else:
            if sizes[i][1] > max_width:
                max_width = sizes[i][1]
            if sizes[i][0] > max_height:
                max_height = sizes[i][0]
    answer = max_width * max_height
    
    return answer