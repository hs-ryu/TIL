n = int(input())
nums = list(map(int,input().split()))
m = int(input())


nums = [0] + nums
dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
    
    # 한자리수는 무조건 펠린드롬
    dp[i][i] = 1
    
    # 11 , 22, 33 처럼 두자리가 같은 경우들
    if i != 1 and nums[i-1] == nums[i]:
        dp[i-1][i] = 1

for i in range(2,n):
    j = 1
    while i + j < n+1:
        if nums[j] == nums[i+j] and dp[j+1][i+j-1] == 1:
            dp[j][i+j] = 1
        j += 1

results = []
for _ in range(m):
    s,e = map(int,input().split())
    results.append(dp[s][e])

for i in range(m):
    print(results[i])