'''
주어진 입력에서 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오.


예를 들어 {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다. 입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.


정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.


print(‘{‘) 같은 경우는 입력으로 주어지지 않으므로 고려하지 않아도 된다.




[입력]


첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50


다음 줄부터 테스트 케이스 별로 온전한 형태이거나 괄호만 남긴 한 줄의 코드가 주어진다.



[출력]


각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


'''



import sys
sys.stdin = open('11572 괄호검사.txt')

def push(value):
    global top
    if top < len(stack) - 1:
        top += 1
        stack[top] = value

def pop():
    global top
    if top >= 0:
        x = stack[top]
        top -= 1
        return x

T = int(input())
for t in range(1, T+1):
    arr = input()
    # '(' 나 '{' 만나면 스택에 집어넣기
    # ')' 나 '}' 만났을때 pop 하는데, pop 한 값이 '('나 '{'가 아니면 잘못된 거니까 result = 0
    # 반복문 다 돌았을때 break 안만나면 result = 1
    top = -1
    stack = [''] * len(arr)
    result = 0
    for i in range(len(arr)):
        if arr[i] == '(':
            push(arr[i])
        elif arr[i] == ')':
            if pop() != '(':
                result = 0
                break
        elif arr[i] == '{':
            push(arr[i])
        elif arr[i] == '}':
            if pop() != '{':
                result = 0
                break
    else:
        if top == -1:
            result = 1
    print('#%d %d' % (t, result))

