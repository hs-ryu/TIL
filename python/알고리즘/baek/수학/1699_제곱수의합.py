# 틀림. 왜틀림?
# n = int(input())
# cnt = 0
# # print(n ** (0.5))
# # print(int(n ** (0.5)))
# while n:
#     x = int(n ** (0.5))
#     n -= x ** 2
#     cnt += 1
# print(cnt)

#dp로 풀기. pypy만 통과
n = int(input())
dp = [x for x in range(n+1)]
for i in range(1,n+1):
    for j in range(1,i):
        if j*j <= i :
            dp[i] = min(dp[i], dp[i-j*j] + 1)
        else:
            break
print(dp[n])

