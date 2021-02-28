'''
문제
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

n=17일때 까지 피보나치 수를 써보면 다음과 같다.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n이 주어진다. n은 20보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄에 n번째 피보나치 수를 출력한다.
'''

# 그냥 일반적인 피보나치.
# 메모리 많이쓴다. 왜냐하면 겹치는것도 또 계산하니까.
# def pibo(n):
#     if n < 2:
#         return n
#     return pibo(n-1) + pibo(n-2)
# n = int(input())
# print(pibo(n))

# 리스트 배열로 피보나치 수열 계산

def pibo(n):
    if n >= 2 and len(pibonachi) <= n:
        pibonachi.append(pibo(n-1) + pibo(n-2))
    return pibonachi[n]
pibonachi = [0,1]
n = int(input())
print(pibo(n))





