# 좌상, 상, 우상 체크
dr = [-1,-1,-1]
dc = [-1,0,1]



n, m = map(int,input().split())
space = [list(map(int,input().split())) for _ in range(n)]

result = 0
for r in range(1,n):
    for c in range(m):
        for k in range(3):
            br = r + dr[k]
            bc = c + dc[k]
            if 0 <= br and 0 <= bc:
                print("??")


print(space)