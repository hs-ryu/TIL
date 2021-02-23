'''
문자열 s에서 반복된 문자를 지우려고 한다. 지워진 부분은 다시 앞뒤를 연결하는데, 만약 연결에 의해 또 반복문자가 생기면 이부분을 다시 지운다.

반복문자를 지운 후 남은 문자열의 길이를 출력 하시오. 남은 문자열이 없으면 0을 출력한다.


다음은 CAAABBA에서 반복문자를 지우는 경우의 예이다.


CAAABBA 연속 문자 AA를 지우고 C와 A를 잇는다.

CABBA 연속 문자 BB를 지우고 A와 A를 잇는다.

CAA 연속 문자 AA를 지운다.

C 1글자가 남았으므로 1을 리턴한다.




[입력]


첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤ 50


다음 줄부터 테스트 케이스의 별로 길이가 1000이내인 문자열이 주어진다.



[출력]


#과 1번부터인 테스트케이스 번호, 빈칸에 이어 답을 출력한다.


'''

import sys
sys.stdin = open('sample_input(7).txt')

# T = int(input())
# for t in range(1, T+1):
#     arr = list(input())
#     i = 0
#     while len(arr) > 0 and i < len(arr) - 1:
#         if arr[i] == arr[i+1]:
#             arr.pop(i)
#             arr.pop(i)
#             i = 0
#         else:
#             i += 1
#     print('#%d %d' %(t, len(arr)))



# 새로운 배열로 만들기
# 계속 스택에 하나씩 푸쉬해 나가면서, top에 있는 놈이랑 집어 넣을 놈이랑 같으면 스택에서 팝.
# 스택에 출력하면됨.
# 스택을 사용하는 방법
def push(v):
    global top
    if top < len(arr):
        top += 1
        stack.append(v)

def pop():
    global top
    if top >= 0:
        temp = stack[top]
        return temp

T = int(input())
for t in range(1, T+1):
    top = -1
    stack = []
    arr = list(input())
    for i in arr:
        if i == pop():
            stack.pop()
            top -= 1
            continue
        push(i)
    print('#%d %d' % (t, len(stack)))