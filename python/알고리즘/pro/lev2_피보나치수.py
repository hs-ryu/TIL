
# dp로 풀기. 재귀로 하면 시간초과남.

import time
start = time.time()

def solution(n):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-2] + dp[i-1]
    answer = dp[n] % 1234567
    return answer
print(solution(10000))
print("time :", time.time() - start)


start = time.time()
def solution1(n):
    dp = [0,1]
    for i in range(2,n+1):
        dp.append(dp[i-1] + dp[i-2])
    answer = dp[n] % 1234567
    return answer
print(solution1(10000))
print("time :", time.time() - start)