'''
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.
'''

# 몇개 숫자 입력 받을건지 결정.
N = int(input())
# N개의 숫자 입력받고
data = list(map(int,input().split()))

# 소수가 아닌놈들을 카운트 해서 전체 길이에서 빼줄거임.
sosux_cnt = 0

# 반복문 돌아서, 3보다 큰 숫자 중에서 2부터 k-1까지 범위중에서 약수가 하나라도 있으면
# 소수가 아니니까 카운트 1씩 증가
for i in range(len(data)):
    if data[i] > 3:
        for j in range(2,data[i]):
            if data[i] % j == 0:
                sosux_cnt += 1
                break
    # 1도 소수가 아니니까 카운트 1 증가
    if data[i] == 1:
        sosux_cnt += 1
# 전체 길이에서 소수가 아닌 놈들을 빼주면 소수의 개수만 남을 것!
result = len(data) - sosux_cnt
print(result)
            

