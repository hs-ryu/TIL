import sys

def InputData():
	readl = sys.stdin.readline
	N = int(readl())
	H = [ int(readl()) for i in range(N) ]
	return N, H

# 입력
# N: 건물 수
# H: 건물 높이
N, H = InputData()
ans = 0

# 코드를 작성 하세요
stack = [0]
H += [10000000000]
for i in range(1,N+1):
	while len(stack) > 0 and H[stack[-1]] <= H[i]:
		temp = stack.pop(-1)
		ans += i-temp-1
	stack.append(i)

# 출력
print(ans)