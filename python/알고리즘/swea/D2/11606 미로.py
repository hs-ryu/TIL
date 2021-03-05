'''
NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오. 도착할 수 있으면 1, 아니면 0을 출력한다.

주어진 미로 밖으로는 나갈 수 없다.


다음은 5x5 미로의 예이다.


13101

10101

10101

10101

10021



마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.




[입력]


첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50


다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 0은 통로, 1은 벽, 2는 출발, 3은 도착이다. 5<=N<=100



[출력]


각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 결과를 출력한다
'''


import sys
sys.stdin = open('sample_input(9).txt')

# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def search(sr, sc):
    global result
    if result == 1:
        return
    if miro[sr][sc] == 3:
        result = 1
        return
    miro[sr][sc] = 1
    for i in range(4):
        r = sr + dy[i]
        c = sc + dx[i]
        if 0 <= r < len(miro) and 0 <= c < len(miro[0]) and miro[r][c] != 1:
            search(r, c)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input())) for i in range(N)]
    result = 0
    #이중 포문에 break 필요한 상황이면 그냥 함수로 빼자
    for i in range(len(miro)):
        for j in range(len(miro[0])):
            if miro[i][j] == 2:
                sr = i
                sc = j
    search(sr, sc)
    print('#%d %d' % (t, result))