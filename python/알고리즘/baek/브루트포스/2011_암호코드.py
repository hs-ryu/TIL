s = list(map(int,input()))
dp = [0] * (len(s) + 1)

if s[0] == 0:
    print(0)
else:
    s = [0] + s
    dp[0] = 1
    dp[1] = 1
    for i in range(2, len(s)):
        if s[i] > 0:
            dp[i] += dp[i-1]
        temp = s[i-1] * 10 + s[i]
        if temp >= 10 and temp <= 26:
            dp[i] += dp[i-2]
    print(dp[len(s)-1] % 1000000)
