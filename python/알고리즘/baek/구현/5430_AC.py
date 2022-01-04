# deque 안쓰면 파이파이만 통과
from collections import deque

t = int(input())
for _ in range(t):
    p = input()
    n = int(input())
    result = ''
    reverse_cnt = 0

    # n이 0이 아닌것 -> 배열에 숫자가 존재하는 상황
    if n != 0:
        # 입력받은 문자열을 숫자만 골라서 배열로 만들어 주기
        nums = deque(map(int,input()[1:-1].split(',')))
        # 상태에 대한 문자열을 돌면서, R을 만나면 바로 뒤집지 말고 카운트 한 뒤 카운트 값이 홀수일때만 최종적으로 뒤집어줌
        # 이렇게 안하고 만날때 마다 뒤집으면 시간초과남.
        for i in range(len(p)):
            if p[i] == 'R':
                reverse_cnt += 1
            else:
                if len(nums) == 0:
                    result = 'error'
                    break
                # 뒤집는 카운트값이 짝수면 현재 원래 상태이므로 왼쪽에서 pop
                if reverse_cnt % 2 == 0:
                    nums.popleft()
                # 홀수면 뒤집어져있는 상태니까 오른쪽에서 pop
                else:
                    nums.pop()
        else:
            # 최종적으로 확인해서 뒤집어줌
            if reverse_cnt % 2:
                nums.reverse()
            # 결과 문자열 만들기
            result = '[' + ','.join(map(str,nums)) + ']'
    # n이 0이면 배열에 숫자가 없음. 따로 처리해준다.
    else:
        nums = input()
        for i in range(len(p)):
            if p[i] == 'D':
                result = 'error'
                break
        else:
            result = '[]'
    print(result)

