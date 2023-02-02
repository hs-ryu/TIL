# 시간초과난다. 다 확인해서 그렇다.
# def search(totalWeight, totalFeel):
#     if totalWeight > k:
#         return
#     if result[0] < totalFeel:
#         result[0] = totalFeel
    
#     for i in range(n):
#         if visited[i] == 0:
#             visited[i] = 1
#             search(totalWeight + goods[i][0], totalFeel + goods[i][1])
#             visited[i] = 0

# n,k = map(int,input().split())
# goods = [list(map(int,input().split())) for _ in range(n)]

# goods.sort(key=lambda x:x[0])
# result = [0]
# visited = [0] * (n+1)
# search(0,0)
# print(result[0])

# 한계 무게를 보면서, 해당 한계 무게때 짐을 넣을 수 있는가?를 본다.
# 한계 무게에서의 최대 가치를 찾아 나가면 된다. 근데, 나중에 확인할 수 있어야하니까 값을 저장하고 있어야한다.
# 음... 
from pprint import pprint

n,k = map(int,input().split())
goods = [0] + [list(map(int,input().split())) for _ in range(n)]
print(goods)
dp = [[0] * (k+1) for _ in range(n+1)]
for limit in range(1,k+1):
    for row in range(1,n+1):
        w,v = goods[row]
        # 현재 물품 무게가 제한 무게보다 크면 못담는다. 이전 최대 무게와 같다.
        if w > limit:
            dp[row][limit] = dp[row-1][limit]
        # 담을 수 있는 경우 -> 그냥 담는게 아니라, 이전것과 비교하여 넣어줘야한다.
        else:
            dp[row][limit] = max(dp[row-1][limit-w]+v, dp[row-1][limit])
pprint(dp)

