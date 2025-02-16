# 흠...
# 완탐 안되네
# 이분탐색?

def solution(diffs, times, limit):
    max_lv = max(diffs)
    min_lv = 1

    while min_lv < max_lv:
        mid_lv = (min_lv + max_lv) // 2
        total = 0
        # print(mid_lv)
        for i in range(len(diffs)):
            if i == 0:
                time_prev = 0
            else:
                time_prev = times[i - 1]

            time_cur = times[i]
            
            if mid_lv >= diffs[i]:
                total +=  time_cur
            else:
                total += (diffs[i] - mid_lv) * (time_cur + time_prev) + time_cur
        # print(total)
        if total <= limit:
            max_lv = mid_lv
        else:
            min_lv = mid_lv + 1
    return min_lv