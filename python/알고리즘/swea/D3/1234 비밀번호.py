'''
평소에 잔머리가 발달하고 게으른 철수는 비밀번호를 기억하는 것이 너무 귀찮았습니다.

적어서 가지고 다니고 싶지만 누가 볼까봐 걱정입니다. 한가지 생각을 해냅니다.

0~9로 이루어진 번호 문자열에서 같은 번호로 붙어있는 쌍들을 소거하고 남은 번호를 비밀번호로 만드는 것입니다.

번호 쌍이 소거되고 소거된 번호 쌍의 좌우 번호가 같은 번호이면 또 소거 할 수 있습니다.

예를 들어 아래의 번호 열을 철수의 방법으로 소거하고 알아낸 비밀 번호입니다.




[입력]

10개의 테스트 케이스가 10줄에 걸쳐, 한 줄에 테스트 케이스 하나씩 제공된다.

각 테스트 케이스는 우선 문자열이 포함하는 문자의 총 수가 주어지고, 공백을 둔 다음 번호 문자열이 공백 없이 제공된다.

문자열은 0~9로 구성되며 문자열의 길이 N은 10≤N≤100이다. 비밀번호의 길이는 문자열의 길이보다 작다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답(비밀번호)을 출력한다.
'''

import sys
sys.stdin = open('input.txt')

# for t in range(1, 11):
#     N, X = input().split()
#     arr = list(X)
#     i = 0
#     while len(arr) > 0 and i < len(arr) - 1:
#         if arr[i] == arr[i+1]:
#             arr.pop(i)
#             arr.pop(i)
#             i = 0
#         else:
#             i += 1
#     print('#%d %s' %(t, ''.join(arr)))

# 새로운 배열로 만들기
# 계속 스택에 하나씩 푸쉬해 나가면서, top에 있는 놈이랑 집어 넣을 놈이랑 같으면 스택에서 팝.
# 스택에 출력하면됨.
# 스택을 사용하는 방법.

def push(v):
    global top
    if top <= len(arr):
        top += 1
        stack.append(v)

def pop():
    global top
    if top >= 0:
        temp = stack[top]
        return temp

for t in range(1, 11):
    N, X = input().split()
    top = -1
    stack = []
    arr = list(X)
    for i in arr:
        if i == pop():
            stack.pop()
            top -= 1
            continue
        else:
            push(i)
    print('#%d %s' %(t, ''.join(stack)))