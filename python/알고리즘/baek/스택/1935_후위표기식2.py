n = int(input())
# 후위식
huwi = list(input())
# 숫자들
nums = [0] * n
# 스택
stack = []
for i in range(n):
    nums[i] = int(input())

for i in range(len(huwi)):
    if 65 <= ord(huwi[i]) <= 90:
        stack.append(nums[ord(huwi[i]) - 65])
        # print(stack)
    else:
        n1 = stack.pop()
        n2 = stack.pop()
        if (huwi[i] == '*'):
            n3 = n2 * n1
        elif (huwi[i] == '+'):
            n3 = n2 + n1
        elif (huwi[i] == '/'):
            n3 = n2 / n1
        elif (huwi[i] == '-'):
            n3 = n2 - n1
        stack.append(n3)
# print(stack[0])
print('{:.2f}'.format(stack[0]))




# 더 짧게 가보자
n = int(input())
# 후위식
huwi = list(input())
# 숫자들
nums = [0] * n
stack = []
for i in range(n):
    nums[i] = input()
    # print(type(nums[i]))
for i in range(len(huwi)):
    if 65 <= ord(huwi[i]) <= 90:
        stack.append(nums[ord(huwi[i]) - 65])
        # print(stack)
    else:
        n1 = stack.pop()
        n2 = stack.pop()
        n3 = eval(n2 + huwi[i] + n1)
        stack.append(str(n3))
print('{:.2f}'.format(float(stack[0])))