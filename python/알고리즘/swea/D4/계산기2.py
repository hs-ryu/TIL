
'''
문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.

예를 들어

“3+4+5*6+7”

라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.

"34+56*+7+"

변환된 식을 계산하면 44를 얻을 수 있다.

문자열 계산식을 구성하는 연산자는 +, * 두 종류이며 피연산자인 숫자는 0 ~ 9의 정수만 주어진다.

[입력]

각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 길이가 주어진다. 그 다음 줄에 바로 테스트 케이스가 주어진다.

총 10개의 테스트 케이스가 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 답을 출력한다.

'''
#괄호, - / 도 있을때를 고려해보기
#중위 -> 후위
#후위를 계산해보는 로직으로
#중위 표기 되어있는 계산 문자열이 있다 : 함수 eval()로 처리가능

import sys
sys.stdin = open('input.txt')

# 중위 -> 후위로 만들기
def change_huwi(sick):
    #후위 계산 방식으로 넣어줄 리스트
    huwi = []
    for x in sick:
        # x가 연산자면
        if x in op:
            # x가 닫는 괄호면, 여는괄호를 만날때 까지 stack에서 연산자들 빼서 후위식에 추가해주기
            if x == ')':
                while stack[-1] != '(':
                    huwi.append(stack.pop())
                # 여는 괄호까지 다 뺐으면, 여는 괄호는 필요 없으니까 stack에서 pop
                stack.pop()
                #다음 반복으로 넘어감
                continue
            # stack 젤 마지막에 있는 연산자보다 우선순위가 높은 연산자라면 stack에 추가해줌
            if out_stack_priority[op.index(x)] > in_stack_priority[op.index(stack[-1])]:
                stack.append(x)
            # stack 젤 마지막에 있는 연산자가 우선순위가 더 높거나 같다면, 
            else:
                # stack 젤 마지막에 있는 연산자의 우선순위가 더 낮을때 까지 pop해서 후위식에 추가해줌.
                while out_stack_priority[op.index(x)] <= in_stack_priority[op.index(stack[-1])]:
                    huwi.append(stack.pop())
                # 더 낮을때까지 pop 했으면 stack에 연산자를 추가해줌
                stack.append(x)
        # x가 피연산자면, 후위식에 그냥 추가. 정수형으로
        else:
            huwi.append(int(x))
    #만약 스택에 연산자가 남아있다면 pop 시켜주기 (단, 첫번째에는 여는 괄호가 들어있으므로 1개 남을때 까지)
    if stack:
        while len(stack) > 1:
            huwi.append(stack.pop())
    return huwi

# 후위 계산
def cal_huwi(huwi):
    cal_stack = []
    for i in huwi:
        #후위식에서 피연산자들을 모두 stack에 넣어줌
        if i not in op:
            cal_stack.append(i)
        #연산자면, 2개를 빼서 연산해줌
        else:
            B = cal_stack.pop()
            A = cal_stack.pop()
            if i == '*':
                x = A * B
            elif i == '/':
                x = A / B
            elif i == '+':
                x = A + B
            else:
                x = A - B
            #계산 끝난 놈들은 stack에 다시 넣어줌.
            cal_stack.append(x)
    #최종적으로 하나밖에 안남았을 거니까 반환해줌
    return int(cal_stack[-1])


op = ['(', '*', '/', '+', '-', ')']
in_stack_priority = [0, 2, 2, 1, 1, 0]
out_stack_priority = [3, 2, 2, 1, 1, 0]

for t in range(1, 11):
    N = int(input())
    sick = input()
    stack = ['(']

    huwi = change_huwi(sick)
    answer = cal_huwi(huwi)

    print('#%d %d' % (t, answer))