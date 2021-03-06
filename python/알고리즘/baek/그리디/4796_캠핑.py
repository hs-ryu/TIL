'''
문제
등산가 김강산은 가족들과 함께 캠핑을 떠났다. 하지만, 캠핑장에는 다음과 같은 경고문이 쓰여 있었다.

캠핑장은 연속하는 20일 중 10일동안만 사용할 수 있습니다.

강산이는 이제 막 28일 휴가를 시작했다. 이번 휴가 기간 동안 강산이는 캠핑장을 며칠동안 사용할 수 있을까?

강산이는 조금 더 일반화해서 문제를 풀려고 한다. 

캠핑장을 연속하는 P일 중, L일동안만 사용할 수 있다. 강산이는 이제 막 V일짜리 휴가를 시작했다. 강산이가 캠핑장을 최대 며칠동안 사용할 수 있을까? (1 < L < P < V)

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있고, L, P, V를 순서대로 포함하고 있다. 
모든 입력 정수는 int범위이다. 마지막 줄에는 0이 3개 주어진다.

출력
각 테스트 케이스에 대해서, 강산이가 캠핑장을 최대 며칠동안 사용할 수 있는지 예제 출력처럼 출력한다.
'''
import sys
sys.stdin = open('test.txt')

i = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V ==0:
        break
    # x = 몫
    x = V // P
    # y = 나머지
    y = V % P
    # 나머지가 몫보다 클 때, 작을 때 분리

    # 1. 몫이 나머지 보다 크다면?
    # 8 12 49   ->  x = 4, y = 1
    # 나머지 1일동안 캠핑할 수 있는 기간 : 1일   -> y
    # 2 12 51   -> x = 4, y = 3
    # 나머지 3일동안 캠핑할 수 있는 기간 : 2일   -> L
    # if x > y:
    if L > y:
        result = L * x + y
    else:
        result = L * x + L
    # 2. 몫이 나머지 보다 작다면?
    # 10 12 21   ->  x = 1, y = 9
    # 나머지 9일동안 캠핑할 수 있는 기간 : 9일  ->  y
    # 8 12 21 -> x = 1, y = 9
    # 나머지 9일동안 캠핑할 수 있는 기간 : 8일  ->  L
    # else:
        # if L > y:
        #     result = L * x + y
        # else:
        #     result = L * x + L
    print('Case %d: %d' %(i,result))
    i += 1
