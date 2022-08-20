n = int(input())

electrics = []

for _ in range(n):
    electrics.append(list(map(int,input().split())))

# 1,8 -> 1~8 사이의 놈들은 8보다 큰 놈과 연결되어야 한다.
# 즉, 정렬했을때, 8,2,9,1,4,6,7,10 일텐데, 최소로 안겹치는 애들은 없애는 것은 최대로 남기는것과 같다.
# 최대로 남기는거 -> 오름차순으로 최대한 남기기.

electrics.sort(key=lambda x:x[0])

dp = [1] * n
for i in range(1,n):
    temp = electrics[i][1]
    for j in range(i):
        prev = electrics[j][1]
        if temp > prev:
            dp[i] = max(dp[i], dp[j] + 1)
# print(dp)
print(n-max(dp))
