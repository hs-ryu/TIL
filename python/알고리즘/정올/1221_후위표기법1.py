m = int(input())
cals = input().split()

calculator = {'+','-','*','/'}
stack = []
for i in cals:
    if i not in calculator:
        stack.append(i)
    else:
        y = int(stack.pop(-1))
        x = int(stack.pop(-1))
        if i == '+':
            z = x + y
        elif i == '-':
            z = x - y
        elif i == '*':
            z = x * y
        elif i == '/':
            z = int(x / y)
        stack.append(z)
print(stack[0])
