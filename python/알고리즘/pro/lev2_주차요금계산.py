def solution(fees, records):
    normal_time, normal_fee, t, t_fee = fees
    
    parking_info = dict()
    # 주차 된 상태라면 1, 주차 안된 상태라면 0
    for i in range(len(records)):
        at_time, car, state = records[i].split()
        if state == "IN":
            if car not in parking_info:
                # 들어온 시간, 통합 요금, 주차 된 상태, 통합 시간(분)
                parking_info[car] = [at_time, 0, 1, 0]
            else:
                parking_info[car][0] = at_time
                parking_info[car][2] = 1
        else:
            parking_info[car][2] = 0
            park_hour, park_minute = map(int,parking_info[car][0].split(":"))
            now_hour, now_minute = map(int,at_time.split(":"))
            park_minute += park_hour * 60
            now_minute += now_hour * 60
            temp_time = now_minute - park_minute
            parking_info[car][0] = "0"
            parking_info[car][3] += temp_time
    for car in parking_info.keys():
        if parking_info[car][2] == 1:
            park_hour, park_minute = map(int,parking_info[car][0].split(":"))
            park_minute += park_hour * 60
            now_minute = 23 * 60 + 59
            temp_time = now_minute - park_minute
            parking_info[car][0] = "0"
            parking_info[car][2] == 0
            parking_info[car][3] += temp_time
        if parking_info[car][3] <= normal_time:
            parking_info[car][1] = normal_fee
        else:
            parking_info[car][1] += normal_fee
            parking_info[car][3] -= normal_time
            if parking_info[car][3] % t:
                parking_info[car][1] += ((parking_info[car][3] // t) + 1) * t_fee
            else:
                parking_info[car][1] += (parking_info[car][3] // t) * t_fee
    x = list(parking_info.items())
    x.sort(key=lambda x:x[0])
    answer = [0] * len(x)
    for i in range(len(x)):
        answer[i] = x[i][1][1]
    
    
    return answer