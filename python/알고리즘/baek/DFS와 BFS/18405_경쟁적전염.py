# 시간초과 풀이...
# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def parasite(r,c,x):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < n:
            if arr[nr][nc] == 0:
                arr[nr][nc] = x


n,k = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

target_time,target_x,targer_y = map(int,input().split())

visited = [[0 for _ in range(n)] for _ in range(n)]

now_time = 0
while now_time < target_time:
    now_time += 1
    num = 1
    while num <= k:
        flag = 0
        for i in range(n):
            for j in range(n):
                if arr[i][j] == num and not visited[i][j]:
                    visited[i][j] = 1
                    parasite(i,j,num)
                    flag = 1
                    break
            if flag:
                break
        num += 1
# print(arr)
print(arr[target_x-1][targer_y-1])
