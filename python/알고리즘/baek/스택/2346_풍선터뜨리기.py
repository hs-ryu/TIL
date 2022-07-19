n = int(input())
balloons = [0] + list(map(int,input().split()))

target = 1
moving = balloons[1]
result = [1]
# 풍선이 터졌는지 안터졌는지 체크
flag = 0
while True:
    if moving > 0:
        while moving:
            if balloons[target] != 0:
                moving -= 1
                target += 1
                if target > n:
                    target = 0
    else:
        while moving < 0:
            if balloons[target] != 0:
                moving += 1
                target -= 1
                if target < 1:
                    target = n
    balloons[target] = 0
    result.append(target)
    
    if not flag:
        break
