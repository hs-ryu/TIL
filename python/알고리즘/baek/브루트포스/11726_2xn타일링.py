# n == 1 -> 1
# n == 2 -> 2
# n == 3 -> 3
# n == 4 -> 5
# n == 5 -> 8
# n == 
# 2 1 1 1, 1 2 1 1, 1 1 2 1, 1 1 1 2, 2 2 1, 1 2 2, 2 1 2, 1 1 1 1 1
# 2 2, 1 1 1 1, 1 2 1, 2 1 1, 1 1 2

# n == 5 -> 
# n == 9 -> 

n = int(input())
dp = [0] * (1001)
dp[1] = 1
dp[2] = 2
for i in range(3,n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007
print(dp[n])