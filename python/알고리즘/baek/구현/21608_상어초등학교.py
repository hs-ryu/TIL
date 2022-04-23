from sys import stdin
input = stdin.readline


dr = [-1,1,0,0]
dc = [0,0,-1,1]

# 좌표 다 돌면서 inf_sit에 주변 친한 사람의 수, 빈 자리의 수, 좌표 싹다 넣어주기
def search_sit():
    for cr in range(n):
        for cc in range(n):
            # 이미 자리에 앉아 있는 놈이 있으면 넘어가
            if sits[cr][cc]:
                continue
            
            # 현재 좌표에서 상하좌우에 빈 자리가 몇갠지, 친한 친구가 몇명인지 체크
            zero_cnt = 0
            freinds_cnt = 0
            for x in range(4):
                nr = cr + dr[x]
                nc = cc + dc[x]
                if 0 <= nr < n and 0<= nc < n:
                    if sits[nr][nc] in good_friends:
                        freinds_cnt += 1
                    if sits[nr][nc] == 0:
                        zero_cnt += 1
            # print(zero_cnt, cr,cc)

            # 자 이제 리스트에 집어넣자.
            inf_sits.append([freinds_cnt, zero_cnt, cr,cc])


n = int(input())
students = [list(map(int,input().split())) for _ in range(n*n)]
# print(students)
sits = [[0] * n for _ in range(n)]
# print(sits)


i = 0
while i < n*n:
    temp_student = students[i][0]
    good_friends = set(students[i][1:])
    # print(good_friends)
    # 주변 친한 사람의 수, 빈 자리의 수, 좌표가 들어갈 리스트
    inf_sits = []

    # inf_sits 채우기.
    search_sit()
    
    # 정렬하자.
    # 1. 좋아하는 학생이 가장 많은 칸.
    # 2. 비어있는 칸이 가장 많은 칸.
    # 3. 행의 번호가 가장 작은 칸.
    # 4. 열의 번호가 가장 작은 칸.
    inf_sits.sort(key=lambda x: (-x[0],-x[1],x[2],x[3]))
    
    # 젤 앞에놈 꺼내서, 그 자리에 집어넣기
    a,b = inf_sits[0][2], inf_sits[0][3]
    sits[a][b] = temp_student

    i += 1


# 만족도 구하기
students.sort(key = lambda x:x[0])
result = 0
for cr in range(n):
    for cc in range(n):
        # 주변 친한친구 수 카운트
        now_person = sits[cr][cc]
        freinds = set(students[now_person-1][1:])

        cnt = 0
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if sits[nr][nc] in freinds:
                    cnt += 1
        
        if cnt == 0:
            continue
        else:
            result += 10 ** (cnt-1)
print(result)
        