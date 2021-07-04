# 오른쪽으로 5개 체크, 오른쪽 대각선 5개 체크, 아래로 5개 체크, 왼쪽 대각선 5개 체크
dr = [0,1,1,1]
dc = [1,1,0,-1]

def omok_check(r,c,color):
    flag = 0
    for i in range(4):
        cnt = 1
        nr = r + dr[i]
        nc = c + dc[i]
        while 0 <= nr < 19 and 0 <= nc < 19 and omok_pan[nr][nc] == color:
            cnt += 1
            if cnt == 5:
                flag = 1
            elif cnt > 5:
                flag = 0
            nr += dr[i]
            nc += dc[i]
        if flag:
            return True
    return False


omok_pan = [list(map(int,input().split())) for _ in range(19)]

result_bl = []
result_wl = []
for i in range(19):
    for j in range(19):
        if omok_pan[i][j] == 1:
            result_b = omok_check(i,j,1)
            if result_b:
                result_bl = [i+1,j+1]
        elif omok_pan[i][j] == 2:
            result_w = omok_check(i,j,2)
            if result_w:
                result_wl = [i+1,j+1]
if result_bl:
    print(1)
    print(*result_bl)
elif result_wl:
    print(2)
    print(*result_wl)
elif result_b == False and result_w == False:
    print(0)