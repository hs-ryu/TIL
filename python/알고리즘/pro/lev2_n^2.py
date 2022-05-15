# 입력이 크기 때문에, n^2 만큼 돌면 시간초과난다.
# 즉, right-left만큼만 돌면서, 규칙을 찾아야한다.
# 규칙을 봤을때, 인덱스의 몫과 나머지를 체크해서 나머지가 몫보다 작을때, 작지 않을 때의 상황으로 구분된다.
# 수학적으로 풀 수 있는 방법에 대해 고민해 본 문제.
def solution(n, left, right):
    answer = [0] * (right+1 - left)
    for i in range(left,right+1):
        x = i // n
        y = i % n
        if y <= x:
            result = x + 1
        else:
            result = 1 + y
        answer[i-left] = result
    return answer