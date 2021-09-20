
# i 번째 일을 할 때의 이익 : pay[i] + dp[i+day[i]]
# i 번째 일을 건너뛰고 i+1번째 일을 할 때의 이익 : dp[i+1]
# 점화식 : dp[i] = max(dp[i+1], pay[i] + dp[i+day[i]])

n = int(input())
day = []
pay = []
dp = []

for i in range(n):
    t,p = map(int, input().split())
    day.append(t)
    pay.append(p)
    dp.append(p)
dp.append(0)

for i in range(n-1, -1, -1):
    if day[i] + i > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], pay[i] + dp[i+day[i]])
print(dp[0])
