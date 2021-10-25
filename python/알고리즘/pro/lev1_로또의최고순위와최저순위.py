def solution(lottos, win_nums):
    answer = []
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    cnt = 0
    cnt_0 = 0
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            cnt += 1
        if lottos[i] == 0:
            cnt_0 += 1
    max_rank = rank[cnt + cnt_0]
    min_rank = rank[cnt]
    answer = [max_rank,min_rank]
    return answer