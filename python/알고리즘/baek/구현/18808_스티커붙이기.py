
import copy

# 넣을수 있는지 확인하고 붙인다.
# 못붙이면 0 리턴. 붙일수 있으면 그 위치들 1로 바꿔주고 1 리턴
def check(cr,cc):

    # 못붙이는지 체크
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1:
                if notebook[cr+i][cc+j] == 1:
                    return False
    # 위가 통과 됐으면 붙일 수 있다는 뜻.
    # 붙이고 True 리턴
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1:
                notebook[cr+i][cc+j] = 1
    return True

# 돌리면서 붙여보기
def turn(flag):
    global sticker, r, c
    if flag:
        turn_stricker = []
        for l in zip(*sticker):
            turn_stricker.append(list(reversed(l)))
        sticker = copy.deepcopy(turn_stricker)
        r,c = len(sticker), len(sticker[0])
    
    for i in range(n):
        if n - i < r:
            break
        for j in range(m):
            if m - j < c:
                break
            if check(i,j):
                return True
    return False



n,m,k = map(int,input().split())

notebook = [[0] * m for _ in range(n)]
for _ in range(k):
    r,c = map(int,input().split())
    sticker = [list(map(int,input().split())) for i in range(r)]
    
    flag = turn(False)
    for i in range(3):
        if not flag:
            flag = turn(True)

# 결과 체크
result = 0
for i in range(n):
    for j in range(m):
        if notebook[i][j]:
            result += 1
print(result)