# 좌상, 상, 우상 체크
dr = [-1,-1,-1]
dc = [-1,0,1]



n, m = map(int,input().split())
space = [list(map(int,input().split())) for _ in range(n)]

# 같은 방향으로 두번 갈 수 없다는거 체크해야함.
result = 0
for r in range(1,n):
    for c in range(m):
        sum_list = []
        for k in range(3):
            br = r + dr[k]
            bc = c + dc[k]
            if 0 <= bc < m:
                sum_list.append(space[r][c] + space[br][bc])
        space[r][c] = min(sum_list)
print(space)

