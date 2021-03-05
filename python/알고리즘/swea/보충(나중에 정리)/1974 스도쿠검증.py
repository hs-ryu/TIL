'''
스도쿠는 숫자퍼즐로, 가로 9칸 세로 9칸으로 이루어져 있는 표에 1 부터 9 까지의 숫자를 채워넣는 퍼즐이다.




같은 줄에 1 에서 9 까지의 숫자를 한번씩만 넣고, 3 x 3 크기의 작은 격자 또한, 1 에서 9 까지의 숫자가 겹치지 않아야 한다.



입력으로 9 X 9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을 때, 위와 같이 겹치는 숫자가 없을 경우, 1을 정답으로 출력하고 그렇지 않을 경우 0 을 출력한다.


[제약 사항]

1. 퍼즐은 모두 숫자로 채워진 상태로 주어진다.

2. 입력으로 주어지는 퍼즐의 모든 숫자는 1 이상 9 이하의 정수이다.


[입력]

입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.

다음 줄부터 각 테스트 케이스가 주어진다.

테스트 케이스는 9 x 9 크기의 퍼즐의 데이터이다.


[출력]

테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''


import sys
sys.stdin = open('input5.txt')

def check():
    cnt = [0] * 10
    for i in range(9):
        for j in range(9):
            pos = BRD[i][j]
            if cnt[pos] == 1:
                return 0

        for j in range(9):
            pos = BRD[j][i]
            if cnt[pos] == 1:
                return 0

    # for c in range(0, 9, 3):
    #     cnt = [0] * 10
    #     for i in range(c, c+3):
    #         for j in range(c, c+3):
    #             pos = BRD[i][j]
    #             if cnt[pos] == 1:
    #                 return 0
    #다시 생각해보기.

T = int(input())
for t in range(1, T+1):
    BRD = [list(map(int, input())) for _ in range(9)]







# import sys
# sys.stdin = open('input5.txt')
#
# T = int(input())
# for t in range(1, T+1):
#     sdocu = []
#     for _ in range(9):
#         sdocu.append(list(map(int, input().split())))
#     sdocu_sero = list(zip(*sdocu))
#     x = {i for i in range(1,10)}
#     idx = 1
#     for i in range(len(sdocu)):
#         if set(sdocu[i]) != x:
#             idx = 0
#             break
#     for i in range(len(sdocu_sero)):
#         if set(sdocu_sero[i]) != x:
#             idx = 0
#             break
#     threebythree = []
#     for i in range(0, 7, 3):
#         for j in range(0, 7, 3):
#             threebythree.append(sdocu[i][j:j+3] + sdocu[i+1][j:j+3] + sdocu[i+2][j:j+3])
#
#     for i in range(len(threebythree)):
#         if set(threebythree[i]) != x:
#             idx = 0
#             break
#     print('#%d %d' % (t, idx))

#
# T = int(input())
# for t in range(1, T+1):
#     sdocu = []
#     for j in range(9):
#         sdocu.append(list(map(int, input().split())))
#     idx = 1
#     # x = {i for i in range(1,10)}
#     x = {1, 2, 3, 4, 5, 6, 7, 8, 9}
#     for j in range(9):
#         w = []
#         if set(sdocu[j]) != x:
#             idx = 0
#             break
#         for k in range(9):
#             w.append(sdocu[k][j])
#         if set(w) != x:
#             idx = 0
#             break
#     for l in range(0, 9, 3):
#         for m in range(0, 9, 3):
#             y = [sdocu[l][m], sdocu[l][m+1], sdocu[l][m+2], sdocu[l+1][m], sdocu[l+1][m+1], sdocu[l+1][m+2], sdocu[l+2][m], sdocu[l+2][m+1], sdocu[l+2][m+2]]
#         if set(y) != x:
#             idx = 0
#             break
#     print('#%d %d' %(t, idx))