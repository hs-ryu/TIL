n = int(input())
if n == 1:
    print(0)
else: 
    jumps = []
    for i in range(n-1):
        jumps.append(list(map(int,input().split())))
    k = int(input())

    dp = [5000 * 21] * n
    dp[0] = 0
    for i in range(n-1):
        one, two = jumps[i]
        if i + 1 < n:
            dp[i+1] = min(dp[i] + one, dp[i+1])
        if i + 2 < n:
            dp[i+2] = min(dp[i] + two, dp[i+2])
        if i + 3 < n:
            dp[i+3] = min(dp[i] + k, dp[i+3])
    print(dp[n-1])
