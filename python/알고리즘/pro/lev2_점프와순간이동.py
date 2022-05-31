# 효율성 0점 코드. dp
def solution(n):
    ans = 0
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1):
        if i % 2 == 0:
            dp[i] = dp[i//2]
        else:
            dp[i] = dp[i-1] + 1
            
    ans = dp[n]
    return ans


# 수학적으로 풀기.
def solution(n):
    ans = 0
    while n != 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            ans += 1
    return ans