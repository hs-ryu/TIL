# 식인종 문제
# 사람 n, 식인종 m, 배에 탈 수 있는 인원 p가 주어진다.
# 식인종 수보다 사람 수가 적으면 식인종이 사람을 잡아먹는다.
# 안전하게 모두 오른 쪽 섬으로 옮길 수 있도록 하는 배 최소 이동 횟수는?
# 배가 이동하면 배에 있는 인원은 모두 내리게 된다.
# 불가능 하다면 -1을 리턴한다.

# 2 <= n,m <= 100
# 1 <= p <= 10
def solution(n,m,p):
    answer = -1
    # 일단 배에 따라 이동할 수 있는 경우의 수를 만들어낸다?
    
    # case1. 식인종을 모두 옮겨라
    # case2. 목사를 모두 옮겨라
    return answer

print(solution(2,2,2)) # 5
print(solution(2,2,1)) # -1
