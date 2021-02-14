'''
문제
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

출력
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
'''
# 시간초과
# N,M = map(int,input().split())
# for i in range(N,M+1):
#     for j in range(2, int(i**(0.5)+1)):
#         if i % j == 0:
#             break
#     else:
#         print(i)

# 소수 판별하는 함수 정의
def sosu(x):
    so = False
    if x == 1:
        return so
    else:
        # 요게 키뽀인트. 어디까지 나누는지
        for i in range(2,int(x**(0.5)+1)):
            if x%i == 0:
                return so
        so = True
        return so
N,M = map(int,input().split())
# 입력 받아서 소수면 출력
for i in range(N,M+1):
    if sosu(i):
        print(i)


