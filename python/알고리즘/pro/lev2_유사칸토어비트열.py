# 시간초과. 규칙을 찾는게 중요할듯.
def solution(n, l, r):
    answer = 0
    dp = ["1"]
    
    for i in range(1,n+1):
        past = dp[i-1]
        temp = ""
        for s in past:
            if s == "1":
                temp += "11011"
            else:
                temp += "00000"
        dp.append(temp)
    x = dp[n]
    for i in range(l-1,r):
        if x[i] == "1":
            answer += 1
    
    return answer