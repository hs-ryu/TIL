# 브루트포스?
from collections import deque
# 핵심: n의 제한이 10000이라서 n^2으로 하면 100% 안된다.
# 한번만 돌면서, 하나씩 더해가면서 확인한다. 단 합이 n보다 크기가 커지는 경우 반복문 돌면서 앞에서부터 빼준다.
# 그러다 합이 n과 같아지면 result에 +1.
# 굳굳
def solution(n):
    answer = 0
    sumVal = 0
    numList = deque([])
    for i in range(1,n+1):
        numList.append(i)
        sumVal += i
        while sumVal > n:
            x = numList.popleft()
            sumVal -= x
        if sumVal == n:
            answer += 1
            
    return answer