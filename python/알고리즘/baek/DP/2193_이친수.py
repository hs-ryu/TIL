n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    dp = [1,1]
    for i in range(1,n+1):
        dp.append(dp[-1] + dp[-2])
    print(dp[n-1])
