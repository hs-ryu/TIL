t = int(input())
k = int(input())

# 5원 3개, 10원 2개, 1원 5개 있다고 하면, 20원을 만들때
# 1원 -> 1가지
# 2원 -> 1가지
# 3원 -> 1가지
# 4원 -> 1가지
# 5원 -> 2가지
# 6원 -> 1가지
# 7원 -> 1가지
# 8원 -> 1가지
# 9원 -> 1가지
# 10원 -> 3가지
# 11원 -> 2가지
# 12원 -> 2가지
# 13원 -> 2가지
# 14원 -> 2가지
# 15원 -> 1 + 1 + 1 + 1가지 -> 4가지
# 16원 -> 1 + 1 -> 2가지
# 17원 -> 2가지
# 18원 -> 2가지
# 19원 -> 2가지
# 20원 -> 1 + 1 + 1 + 1 -> 4가지

# 규칙 못찾겠다...
moneys = []
for _ in range(k):
    moneys.append(list(map(int,input().split())))
moneys.sort(key=lambda x:x[0], reverse=True)
dp = [0] * 10001
dp[0] = 1
for i in range(k):
    money, cnt = moneys[i]
    for j in range(t,-1,-1):
        m = 1
        while m <= cnt and j - money * m >= 0:
            dp[j] += dp[j - money * m]
            m += 1
print(dp[t])