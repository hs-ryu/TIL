# 1퍼에서 틀림.
n = int(input())

jumps = []
for i in range(n-1):
    jumps.append(list(map(int,input().split())))
k = int(input())

# dp 돌리면서, 입력 받은 작은점프, 큰점프, 매우 큰점프로 최소값 구해주기.
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
# 젤 끝에놈 출력. 근데 왜 틀리지.
print(dp[n-1])
