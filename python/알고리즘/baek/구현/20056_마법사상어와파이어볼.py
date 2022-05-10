# 위, 오위, 오, 오아, 아, 왼아, 왼, 왼위

from copy import deepcopy

dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

# bfs ㄱ
def move(jido):
    new_jido = [[[] * n for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if jido[i][j]:
                
                while jido[i][j]:
                    r,c,m,s,d,flag = jido[i][j].pop(0)
                    # 이미 이동한 애인가? 그럼 이동 안시킨다
                    if flag:
                        new_jido[i][j].append([r,c,m,s,d,flag])
                    else:
                        nr,nc = r + (dr[d] * s), c + (dc[d] * s)
                        while nr < 0:
                            nr += n
                        while nr >= n:
                            nr -= n
                        while nc < 0:
                            nc += n
                        while nc >=n:
                            nc -= n
                        flag = 1
                        new_jido[nr][nc].append([nr,nc,m,s,d,flag])
    return new_jido
    
n,m,k = map(int,input().split())
jido = [[[] * n for _ in range(n)] for _ in range(n)]
# print(jido)
for _ in range(m):
    fireball = list(map(int,input().split()))
    fireball[0] -= 1
    fireball[1] -= 1
    # 이미 이동한 애인지에 대한 플래그 추가
    fireball.append(0)
    jido[fireball[0]][fireball[1]].append(fireball)

# 조건에 맞춰 ㄱ
while k:
    # 파이어볼 이동시키기. 굳!
    jido = deepcopy(move(jido))

    fireballs = []
    # 그러면서 이동 플래그 다 0으로 초기화
    for i in range(n):
        for j in range(n):
            if jido[i][j]:
                for l in range(len(jido[i][j])):
                    jido[i][j][l][5] = 0
                    fireballs.append(jido[i][j][l])
    # 겹치는 파이어볼 나누기.             
    while fireballs:
        r,c,m,s,d,flag = fireballs.pop(0)
        # 겹치는 애들 체크
        cnt = 0
        for i in range(len(fireballs)):
            other_r, other_c = fireballs[i][0], fireballs[i][1]
            if other_r == r and other_c == c:
                cnt += 1
        cnt -= 1
        # 하 어떻게 겹치는 애들을 fireballs 리스트에서 없앨까....?
        
        if cnt >= 2:
            pass

    


    k -= 1