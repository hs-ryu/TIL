'''
문제
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

출력
N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.
'''
# def sosu(x):
#     so = False
#     if x == 2 or x == 3:
#         so = True
#         return so
#     for i in range(2,int(x/2)+1):
#         if x % i == 0:
#             so = False
#             break
#     else:
#         so = True
#     return so


# 너무 비효율적이다. 소수만 골라서 나누고 싶은데....
N = int(input())
for i in range(2, N+1):
    if N%i == 0:
        while N%i == 0:
            print(i)
            N //= i

    