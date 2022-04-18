n = int(input())

k = [0] * (n+5)
k[1] = 1
k[0] = 1
i = 2

while True:
    if i > n+4:
        break
    # 짝수일때
    # 홀수 년, 짝수년에 태어난 세포는 모두 짝수년에 소멸함.
    if i % 2 == 0:
        k[i] = k[i-1] * 2 - k[i-4] - k[i-5]
    else:
        k[i] = k[i-1] * 2
            
    i += 1
# print(k)
print(k[n])

# n=int(input())
# dp = [0 for _ in range(21)]
# dp[0]=1
# dp[1]=1
# for i in range(2, 21):
#     if i%2 == 0:
#         dp[i] = dp[i-1] * 2 - dp[i-4] - dp[i-5]
#     else:
#         dp[i] = dp[i-1] * 2
# print(dp[n])
