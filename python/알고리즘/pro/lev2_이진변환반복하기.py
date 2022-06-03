def solution(s):
    answer = [0,0]
    t = 0
    s = list(s)
    cnt = 0
    while True:
        len_s = len(s)
        if len_s == 1:
            break
        x = s.count("1")
        y = "1" * x
        cnt += len_s - x
        len_y = len(y)
        s = list(bin(len_y)[2:])
        t += 1
    if cnt or t:
        answer[0], answer[1] = t,cnt
    return answer