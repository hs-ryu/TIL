import sys

def InputData():
	readl = sys.stdin.readline
	B, S, D = readl().strip().split()
	return int(B), S, D

# 10진수 수를 B진수 문자로 변경.
def IntToB(number, target):
	text = [str(i) for i in range(10)] + [chr(i) for i in range(65,91)]
	result = ""
	while number > 0:
		number, r = divmod(number, target)
		result = text[r] + result	
	return result if result else "0"
# 입력

# N : 테스트 케이스 수
# B : 진법
# S : 첫 번째 정수
# D : 두 번째 정수


N = int(input())
for _ in range(N):
	B, S, D = InputData()
	# 코드를 작성 하세요
	# 접근법 : B진수 -> 10진수 -> 연산 -> B진수
	# 음수 갈라주기.
	minus = 0
	if S[0] == "-":
		minus += 1
		S = S[1:]
	if D[0] == "-":
		minus += 1
		D = D[1:]
	
	# S,D 값을 10진수로 변환
	s = 0
	for i in range(len(S)):
		# A ~ Z 면은
		if 65 <= ord(S[i]) < 91:
			s += (ord(S[i]) - 65 + 10) * B**(len(S)-i-1)
		else:
			s += int(S[i]) * B**(len(S)-i-1)
	
	d = 0
	for i in range(len(D)):
		if 65 <= ord(D[i]) < 91:
			d += (ord(D[i]) - 65 + 10) * B ** (len(D)-i-1)
		else:
			d += int(D[i]) * B ** (len(D) - i - 1)
	# 변환한 각각의 값을 곱합.
	multi = s * d
	# 계산된 결과값을 B진수로 변환.
	ans = IntToB(multi, B)
	
	if minus % 2 == 1 and ans != "0":
		ans = "-" + ans
	
	# 출력
	print(ans)