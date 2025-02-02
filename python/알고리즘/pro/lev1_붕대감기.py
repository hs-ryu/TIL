# bandage = [t, x, y]
# health = 최대 체력
# attacks = [공격시간, 피해량]

def solution(bandage, health, attacks):
    time = 1
    answer = health
    for i in range(len(attacks)):
        at, dil = attacks[i]
        
        # 딜 쳐맞기 전에 상태 업데이트
        during = at - time
        
        add = during // bandage[0]
        tic = during * bandage[1]
        total_heal = add * bandage[2] + tic
        
        if answer + total_heal >= health:
            answer = health
        
        # 딜 타임
        answer = answer - dil
        time = at + 1
        
        # 캐릭터 뒤질때
        if answer - dil < 0:
            answer = -1
            break
    
    return answer