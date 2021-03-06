'''
N X N크기의 농장이 있다.

이 농장에는 이상한 규칙이 있다.

규칙은 다음과 같다.


   ① 농장은 크기는 항상 홀수이다. (1 X 1, 3 X 3 … 49 X 49)

   ② 수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태로만 가능하다.

1 X 1크기의 농장에서 자라는 농작물을 수확하여 얻을 수 있는 수익은 3이다.

3 X 3크기의 농장에서 자라는 농작물을 수확하여 얻을 수 있는 수익은 16 (3 + 2 + 5 + 4 + 2)이다.

5 X 5크기의 농장에서 자라는 농작물의 수확하여 얻을 수 있는 수익은 25 (3 + 2 + 1 + 1 + 2 + 5 + 1 + 1 + 3 + 3 + 2 + 1)이다.

농장의 크기 N와 농작물의 가치가 주어질 때, 규칙에 따라 얻을 수 있는 수익은 얼마인지 구하여라.

[제약 사항]

농장의 크기 N은 1 이상 49 이하의 홀수이다. (1 ≤ N ≤ 49)

농작물의 가치는 0~5이다.


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스에는 농장의 크기 N과 농장 내 농작물의 가치가 주어진다.


[출력]

각 줄은 '#t'로 시작하고, 공백으로 농장의 규칙에 따라 얻을 수 있는 수익을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

'''


import sys
sys.stdin = open('input3.txt')

# 방법1. 전체 합에서 각 모서리에서 부분의 합을 빼버리기
# 방법2. N//2의 범위를 빼버린다.   <- 채택
# N = 7인경우, 2로나눈 몫이 3이므로,  왼쪽 모서리만 보면 3-i + 3-j가 3보다 같거나 작은경우, 마름모 꼴에 해당한다.
# 따라서 모든 모서리를 고려해줘야하니까 절대값으로 계산하면 될듯.

# T = int(input())
# def absolute(x):
#     if x < 0:
#         x *= (-1)
#     return x
# for t in range(1, T+1):
#     N = int(input())
#     k = N //2
#     result = 0
#     farm = [list(map(int, input())) for _ in range(N)]
#     for i in range(len(farm)):
#         for j in range(len(farm[0])):
#             if absolute(k-i) + absolute(k-j) >= k:
#                 result += farm[i][j]
#     print(result)





















def absolute(x):
    if x < 0:
        return x * (-1)
    return x


def suhwack(farm):
    result = 0
    X = len(farm)
    for i in range(X):
        for j in range(X):
            k = X // 2
            if absolute(k-i) + absolute(k-j) <= k:
                result += farm[i][j]
    return result


T = int(input())
for t in range(1,T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    print('#%d %d' % (t, suhwack(farm)))