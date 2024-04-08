N, ATK = map(int, input().split())

info = [list(map(int, input().split())) for _ in range(N)]

l = 0
r = 1000000 * 1000000 * 123456


result = 0
# 시간 복잡도 = 123456 * log(100000*1000000)
while l <= r:
    ATK_copy = ATK
    MaxHP = (l + r) // 2
    isDie = False
    CurHP = MaxHP
    for i in range(N):
        t,a,h = info[i]
        # t = 2라면 포션 및 버프
        if t == 2:
            ATK_copy += a
            CurHP = min(MaxHP, CurHP + h)
        # t = 1 이라면 계산 해야지.
        elif t == 1:
            # 용사가 한대 쳐서 죽는다 -> 용사 피는 안깎인다.
            # 용사가 두대 쳐서 죽는다 -> 용사 피는 1번 깎인다.
            # 용사가 N번 쳐서 죽는다 -> 용사 피는 N-1번 깎인다.

            # 용의 피가 30, 용사의 데미지가 31 -> 30 // 31 = 0
            # 용의 피가 30, 용사의 데미지가 29 -> 30 // 29 = 1
            # 용의 피가 30, 용사의 데미지가 30 -> 30 // 30 = 1 이지만, 딱뎀으로 죽일 수 있으니깐, 안맞음.
            # 용사의 피가 깎이는 횟수 = 용의 피 // 용사의 데미지

            CurHP -= a * ((h // ATK_copy)) if h % ATK_copy else a * ((h // ATK_copy)-1) # 만약 딱댐으로 죽일 경우는 한대 덜 때린다.
            # print(CurHP)
            if CurHP <= 0:
                isDie = True
                break
            
        # print(ATK_copy, MaxHP, CurHP,  l, r, isDie)
    # print("-----------")
    # 만약 용사가 죽는 상황이면 -> MaxHP를 키워줘야함.
    if isDie:
        l = MaxHP + 1
    # 안죽는 상황이면 -> 일단 값을 저장해 놓고 최소의 경우를 찾기위해 더 탐색
    else:
        r = MaxHP - 1
        result = MaxHP
    
print(result)





# 1번방 입장 = 피 48
# 16번 때림. -> 15번 맞음 - 15 깎임
# 15 깎임 -> 33 남음
# 2번방 입장 = 피 33
# 피 43, 공격력 6
# 3반벙 입장 = 17번 때림 -> 16번 맞음 - 48 깍임
# 뒤져야하는데?
print(1000000000000 - 1000000)