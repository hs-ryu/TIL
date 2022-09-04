# [상,우,하,좌]
# 1 : 오른쪽, 2: 양 옆, 3: 위 오른, 4: 양옆 위, 5: 사방
# 90도 회전 -> 1: 아래, 2: 위아래, 3: 오른,아래, 4: 위아래, 오른, 5: 사방

from pprint import pprint
dir = [[],[0,1,0,0],[0,1,0,1],[1,1,0,0],[1,1,0,1],[1,1,1,1]]

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def search(level, arr):
    if level == len(cctvs):
        # 다 돌았으면, 빈 공간 체크하기.
        cnt = 0
        # pprint(arr)
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    cnt += 1
        global result
        result = min(result, cnt)
        return

    # cctv 하나씩 선택하기.
    for i in range(level,len(cctvs)):
        temp_cctv = cctvs[i]
        temp_dir = dir[temp_cctv[2]]
        # 90도씩 돌리면서, 체크하기.
        for j in range(4):
            arr_copy = []
            for p in range(n):
                arr_copy.append(arr[p][:])
            temp_dir_0 = temp_dir[0]
            temp_dir_1 = temp_dir[1]
            temp_dir_2 = temp_dir[2]
            temp_dir_3 = temp_dir[3]
            temp_dir[0] = temp_dir_3
            temp_dir[1] = temp_dir_0
            temp_dir[2] = temp_dir_1
            temp_dir[3] = temp_dir_2
            # 여기서 cctv 놓고 체크하고, 재귀 돌리자.
            for k in range(4):
                if temp_dir[k] == 1:
                    cr = temp_cctv[0] + dr[k]
                    cc = temp_cctv[1] + dc[k]
                    while 0<=cr<n and 0<=cc<m:
                        # print(cr,cc)
                        if arr_copy[cr][cc] == "#":
                            cr += dr[k]
                            cc += dc[k]
                        elif 1<=arr_copy[cr][cc]<=5:
                            cr += dr[k]
                            cc += dc[k]
                        elif arr_copy[cr][cc] == 6:
                            break
                        elif arr_copy[cr][cc] == 0:
                            arr_copy[cr][cc] = "#"
                            cr += dr[k]
                            cc += dc[k]
                        else:
                            cr += dr[k]
                            cc += dc[k]
            search(level+1, arr_copy)


n, m = map(int,input().split())


office = []
for _ in range(n):
    office.append(list(map(int,input().split())))

cctvs = []
for i in range(n):
    for j in range(m):
        if office[i][j] != 0 and office[i][j] != 6:
            cctvs.append([i,j,office[i][j]])
result = 65
search(0, office)
print(result)