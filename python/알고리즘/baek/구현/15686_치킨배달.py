def search(level, arr, k):
    if k == len(chickens):
        return
    if level == m:
        # 여기서 길이 체크하기.
        return
    
    for i in range(k, len(chickens)):
        pass


n,m = map(int,input().split())

city = []
for i in range(n):
    city.append(list(map(int,input().split())))

# 1. 치킨집의 위치를 다 찾는다. 집의 위치도 미리 다 찾아 놓는다.
# 2. 치킨집 중에서 m개를 고른다. (조합)
# 3. 집에서 치킨집의 위치를 정한다.

homes = []
chickens = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            homes.append([i,j])
        elif city[i][j] == 2:
            chickens.append([i,j])