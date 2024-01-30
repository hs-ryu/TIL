import math

def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    
    # 각 초마다 계산했을때 23 * 59 * 59 < 100 * 100 * 100 = 1,000,000
    # 현재 시간, 종료 시간을 초로 계산해서, 1씩 증가시키면서 계산해보자.
    
    # 1초의 각도 : 360 / 60 = 6도
    
    # 5분의 각도 : 360 / 12 = 30도
    # 1분의 각도 : 360 / 60 = 6도
    # 1초당 분침이 움직이는 각도 : 6도 / 60 = 0.1도
    
    # 1시간의 각도 : 30도
    # 1분당 시침이 움직이는 각도 : 10 / 20 = 0.5도
    # 1초당 시침이 움직이는 각도 : 5 / 600 = 1/120도 
    
    # 즉, 1초씩 늘어날건데, 분침의 현재 각도 < 초침의 현재 각도가 되는 순간 +1
    # OR 시침의 현재 각도 < 초침의 현재 각도가 되는 순간 + 1
    
    nowTime = h1 * 3600 + m1 * 60 + s1
    endTime = h2 * 3600 + m2 * 60 + s2
    
    hAngle = 1 / 120 * nowTime % 360
    mAngle = 6 / 60 * nowTime % 360
    sAngle = 6.0 * nowTime % 360
    
    print(nowTime, endTime)
    print(hAngle, mAngle, sAngle)
    if hAngle == mAngle == sAngle:
        answer += 1
    
    while nowTime != endTime:
        # 만약, 현재 초침의 각도가 분침의 각도보다 작은데, 1초 증가했을때 분침의 각도보다 커진다면? + 1
        if nowTime == 43199:
            print(sAngle, mAngle, hAngle)
        if sAngle < mAngle:
            if nowTime == 43199:
                print(sAngle + 6, mAngle + 0.1)
            if sAngle + 6.0 >= mAngle + 0.1:
                answer += 1
        # 만약, 현재 초침의 각도가 시침의 각도보다 작은데, 1초 증가했을때 시침의 각도보다 커진다면? + 1
        if sAngle < hAngle:
            if sAngle + 6.0 >= hAngle + 1/120:
                answer += 1
        # 시침과 분침이 만나는 시점은 0시 0분 0초, 12시 0분 0초. 두가지 경우. 이때는 위에서 중복 계산 될것이기 때문에 -1 해준다.
        nowTime += 1
        if nowTime == 12 * 3600:
            answer -= 1
        sAngle = (sAngle + 6) % 360
        mAngle = (mAngle + 0.1) % 360
        hAngle = (hAngle + 1/120) % 360
    
    return answer