# import math
# n, m = map(int, input().split())
# n -= m
# n = abs(n)
# m = math.factorial
# print(m(2 * n) // m(n) // m(n) // (n+1))



n, m = map(int,input().split())

if n == m:
    print(1)

else:

    if m > n:
        n,m = m,n

    m -= n
    m = abs(m)
    n = 0

    dp = [[0] * (m+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[0][i] = 1

    # print(dp)
    for i in range(1,m+1):
        for j in range(m+1):
            if j < i:
                continue
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
    print(dp[m][m])



