# dp 문제.
# 주어진 배열과 똑같은 크기의 dp 배열 하나 만들고, 차근차근 내려오면서 max값만 dp 배열에 남긴다.
# 행의 맨 첫값과 마지막 값은 바로 위의 값에다 현재 값을 더한것과 같다는 조건 처리가 필수.
def solution(triangle):
    dp = []
    for i in range(len(triangle)):
        dp.append([0] * len(triangle[i]))
    dp[0][0] = triangle[0][0]
    
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == len(triangle[i]) - 1:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + triangle[i][j], dp[i-1][j] + triangle[i][j])
            
    
    return max(dp[-1])