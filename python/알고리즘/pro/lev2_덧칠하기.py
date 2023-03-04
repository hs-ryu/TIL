def solution(n, m, section):
    answer = 0
    painted = 0
    for i in range(len(section)):
        # 마지막으로 페인트 칠 된 곳을 확인해서, 그것보다 작으면 칠 안된것이니까 갱신.
        if painted < section[i]:
            painted = section[i] + m - 1
            answer += 1
    return answer