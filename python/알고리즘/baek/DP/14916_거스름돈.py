# 2 -> 2원 1
# 4 -> 2원 2
# 5 -> 5원 1


n = int(input())


dp = [n] * 100001
dp[2] = 1
dp[4] = 2
dp[5] = 1

for i in range(6,n+1):
    dp[i] = min(dp[i-2], dp[i-5]) + 1
    # print(dp)
if (dp[n] != n):
    print(dp[n])
else:
    print(-1)