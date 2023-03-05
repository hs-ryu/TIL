
# 안된다 안돼! 
def solution(sequence):
    answer = 0
    # 순서대로 확인해보면서, 큰것을 확인해보는 것. dp.
    dp = [0] * len(sequence)
    lastMul = 1
    dp[0] = max(sequence[0], -sequence[0])
    if sequence[0] > 0:
        lastMul = 1
    else:
        lastMul = -1
    for i in range(1,len(sequence)):
        # 이전에 곲한 값이 1이라면?
        # 현재 값에 -1을 곱한값을 이전값과 더한것과, 현재 값에 1을 곱한 값을 비교한다.
        # 현재 값에 -1을 곱한값을 이전값과 더한것이 더 크다면? lastMul을 -1로 변경한다.
        # 현재 값에 1을 곱한 값이 더 크다면? lastMul을 1로 한다.
        if lastMul == 1:
            if -sequence[i] + dp[i-1] >= sequence[i]:
                dp[i] = -sequence[i] + dp[i-1]
                lastMul = -1
            else:
                dp[i] = sequence[i]
                lastMul = 1
        else:
            if sequence[i] + dp[i-1] >= -sequence[i]:
                dp[i] = sequence[i] + dp[i-1]
                lastMul = 1
            else:
                dp[i] = -sequence[i]
                lastMul = -1
    answer = max(dp)
    
    return answer

def solution(sequence):
    answer = 0
    # dp[n] = Max(dp[n-1]+n번째숫자(n값의 따른 음수 또는 양수), n번째숫자(n값의 따른 음수 또는 양수))
    # 즉, 2개의 dp 배열을 사용해서, 하나는 처음 값에 1을 곱한것, 하나는 처음 값에 -1을 곱한것으로 둔다.
    # 이후, 반복문을 통해서 하나하나 체크하는데. 현재값에 -1 혹은 1을 곱한 값과 이전 값을 더한 것, 현재 값에 -1 혹은 1을 곱한 값을 비교하여 갱신한다.
    # 이렇게하면 고려하지 않는 부분이 없을까? 없다. 왜냐면 2개의 dp 배열을 쓰니까. 현재 값에 -1이나 1을 곱한 값은 2개의 dp 배열을 통해 체크가 가능하기 때문에 상관이 없다.
    dp_plus = [0] * len(sequence)
    dp_minus = [0] * len(sequence)
    flag = 1
    dp_plus[0] = sequence[0]
    dp_minus[0] = -sequence[0]
    
    for i in range(1,len(sequence)):
        flag *= -1
        dp_plus[i] = max(dp_plus[i-1] + sequence[i] * flag, sequence[i] * flag)
        dp_minus[i] = max(dp_minus[i-1] + sequence[i] * (-flag), sequence[i] * (-flag))

    answer = max(max(dp_plus),max(dp_minus))
    return answer