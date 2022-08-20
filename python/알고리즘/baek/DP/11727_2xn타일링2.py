n = int(input())

dp = [0,1,3]
for i in range(3,n+1):
    dp.append((dp[i-1] + dp[i-2] * 2) % 10007)
print(dp[n])

# n = 1 -> 1
# n = 2 -> 3
# n = 3 -> 5
# n = 4 -> 11
# n = 5 -> 21
# n = 6 -> 43
# n = 7 -> 85
# n = 8 -> 171