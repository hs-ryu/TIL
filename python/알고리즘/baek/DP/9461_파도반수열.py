t = int(input())
# 쉽다 쉬워. 그냥 i-3 + i-2네.
for _ in range(t):
    n = int(input())
    dp = [0] * (101)
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    if n < 4:
        print(dp[n])
    else:
        for i in range(4,n+1):
            dp[i] = dp[i-3] + dp[i-2]
        # print(dp)
        print(dp[n])
