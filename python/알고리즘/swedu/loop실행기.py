import sys

def input_data():
	readl = sys.stdin.readline
	loop = readl().strip()
	return loop


# 입력 받는 부분
loop = input_data()

# 코드를 작성하세요
nums = {str(i) for i in range(10)}
result = ""
stack = []

for i in range(len(loop)):
	if loop[i] == ">":
		temp = stack.pop(-1)
		s = ""
		while temp not in nums:
			s = temp + s
			temp = stack.pop(-1)
		stack.pop(-1)
		stack.append(s * int(temp))
		
	else:
		stack.append(loop[i])

if len(stack):
	print(stack[0])
else:
	print("")
			
			