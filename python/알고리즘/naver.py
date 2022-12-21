# 전구 켜기. 3,4,5,1,2 순으로 켜면?
# 총 2번에 걸쳐 켜진다.

def solution(burbs):
    result = 0
    
    # cnt = 1
    # lastNum = 1
    # for i in range(len(lights)):
    #     if lights[i] == cnt:
    #         result += 1
    #         cnt = lastNum + 1
    #         lastNum = cnt
    #     elif lastNum < lights[i]:
    #         lastNum = lights[i]

    on = 0
    waiting = set()
    for i in range(len(burbs)):
        # 만약 현재 켜려는 전구가 켜저있는 바로 다음 전구라면?
        # 켜지고, 켜지길 기다리는 전구들도 체크해준다. 1,3,4,5,2 순이라면 2가 켜질때 waiting에 3,4,5가 들어있을거다.
        # 얘네도 다 켜줘야한다. 켜 주고, wating에서 삭제해준다.
        if burbs[i]-1 == on:
            on = burbs[i]
            result += 1
            while True:
                nextBurb = on + 1
                if nextBurb in waiting:
                    waiting.remove(nextBurb)
                    on = nextBurb
                else:
                    break
        # 아니라면, wating에 집어넣는다.
        else:
            waiting.add(burbs[i])
    return result

x = [5,3,2,1,4] # 2
y = [1,3,4,2,5] # 3
z = [3,4,5,1,2]
k = [5,4,3,2,1]
q = [1,2,3,4,5]
w = [1,3,6,2,4,5]
p = solution(w)
print(p)