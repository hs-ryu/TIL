def search(level, arr):
    if level == len(chickens):
        if len(arr) == m:
            # 여기서 체크하면 될듯. 2중 반복문 써서, 가까운 애들 쳌 해버리자.
            # print(arr)
            global result
            temp_result = 0
            for i in range(len(homes)):
                # 집 하나하나에서 부터 가까운 치킨집 거리 구하기.
                temp_home = homes[i]
                temp_total_length = 101
                for j in range(len(arr)):
                    temp_chicken = arr[j]
                    # print("현재 체크 집, 치킨집 : ", temp_home, temp_chicken)
                    temp_length = abs(temp_home[0] - temp_chicken[0]) + abs(temp_home[1] - temp_chicken[1])
                    temp_total_length = min(temp_total_length,temp_length)
                temp_result += temp_total_length
            result = min(temp_result, result)
        return
    arr.append(chickens[level])
    search(level+1,arr)
    arr.pop(-1)
    search(level+1,arr)



n,m = map(int,input().split())

city = []
for i in range(n):
    city.append(list(map(int,input().split())))

# 1. 치킨집의 위치를 다 찾는다. 집의 위치도 미리 다 찾아 놓는다.
# 2. 치킨집 중에서 m개를 고른다. (조합)
# 3. 집에서 치킨집의 위치를 정한다.

homes = []
chickens = []
result = 101 * 14
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            homes.append([i,j])
        elif city[i][j] == 2:
            chickens.append([i,j])
# print(chickens)
search(0,[])
print(result)