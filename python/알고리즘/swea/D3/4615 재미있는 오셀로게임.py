'''
오셀로라는 게임은 흑돌과 백돌을 가진 사람이 번갈아가며 보드에 돌을 놓아서 최종적으로 보드에 자신의 돌이 많은 사람이 이기는 게임이다.

보드는 4x4, 6x6, 8x8(가로, 세로 길이) 크기를 사용한다. 6x6 보드에서 게임을 할 때, 처음에 플레이어는 다음과 같이 돌을 놓고 시작한다(B : 흑돌, W : 백돌).

4x4, 8x8 보드에서도 동일하게 정가운데에 아래와 같이 배치하고 시작한다.



그리고 흑, 백이 번갈아가며 돌을 놓는다.

처음엔 흑부터 시작하는데 이 때 흑이 돌을 놓을 수 있는 곳은 다음과 같이 4군데이다.



플레이어는 빈공간에 돌을 놓을 수 있다.

단, 자신이 놓을 돌과 자신의 돌 사이에 상대편의 돌이 있을 경우에만 그 곳에 돌을 놓을 수 있고, 그 때의 상대편의 돌은 자신의 돌로 만들 수 있다.

(여기에서 "사이"란 가로/세로/대각선을 의미한다.)

(2, 3) 위치에 흑돌을 놓은 후의 보드는 다음과 같다.



이런 식으로 번갈아가며 흑, 백 플레이어가 돌을 놓는다.

만약 돌을 놓을 곳이 없다면 상대편 플레이어가 다시 돌을 놓는다.

보드에 빈 곳이 없거나 양 플레이어 모두 돌을 놓을 곳이 없으면 게임이 끝나고 그 때 보드에 있는 돌의 개수가 많은 플레이어가 승리하게 된다.


 [입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 보드의 한 변의 길이 N과 플레이어가 돌을 놓는 횟수 M이 주어진다. N은 4, 6, 8 중 하나이다.

그 다음 M줄에는 돌을 놓을 위치와 돌의 색이 주어진다.

돌의 색이 1이면 흑돌, 2이면 백돌이다.

만약 3 2 1이 입력된다면 (3, 2) 위치에 흑돌을 놓는 것을 의미한다.

돌을 놓을 수 없는 곳은 입력으로 주어지지 않는다.

 [출력]

각 테스트 케이스마다 게임이 끝난 후 보드 위의 흑돌, 백돌의 개수를 출력한다.

흑돌이 30개, 백돌이 34인 경우 30 34를 출력한다.

'''
#함수 안쓰고 풀기
# import sys
# sys.stdin = open('sample_input(1).txt')
#
#
# dx = [-1, 1, 0, 0, -1, 1, -1, 1] # 왼쪽, 오른쪽, 아래, 위, 왼쪽위 대각, 오른쪽위 대각, 왼쪽 아래 대각, 오른쪽 아래대각
# dy = [0, 0, 1, -1, -1, -1, 1, 1]
#
# T = int(input())
# for t in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [[0 for i in range(N)] for i in range(N)]
#     arr[N//2][N//2], arr[N//2-1][N//2-1] = 'W', 'W' # 초기 흰돌이 놓여있는 상황
#     arr[N//2][N//2-1], arr[N//2-1][N//2] = 'B', 'B' # 초기 검돌이 놀여있는 상황
#     for i in range(M):
#         turn = list(map(int, input().split()))
#         #돌 놓기
#         arr[turn[0]-1][turn[1]-1] = 'B' if turn[2] == 1 else 'W'
#         #놓은 돌을 기준으로 바꿔야 할거 찾아서 바꾸기.
#         #놓은 돌이 흑돌일 경우
#         if arr[turn[0]-1][turn[1]-1] == 'B':
#             # 왼쪽, 오른쪽, 아래, 위, 왼쪽위 대각, 오른쪽위 대각, 왼쪽 아래 대각, 오른쪽 아래대각 순으로 탐색
#             for j in range(8):
#                 white_list = []
#                 x = turn[0] - 1
#                 y = turn[1] - 1
#                 #좌표 이동했을때, 해당 좌표가 arr 내부에 있다면 계속 그 방향으로 탐색
#                 while 0 <= x + dy[j] < len(arr) and 0 <= y + dx[j] < len(arr):
#                     x += dy[j]
#                     y += dx[j]
#                     # 흑돌, 백돌이 놓여있는 부분 이외에는 다 0이므로, 탐색하다 0을 만나면 while문 탈출 (돌과 돌사이에 빈공간이 있는 경우는 의미 없으므로)
#                     if arr[x][y] == 0:
#                         break
#                     #탐색을 하는데 돌이 있다면?
#                     else:
#                         # 탐색 좌표에 있는 돌이 백돌일 경우, 흑돌과 흑돌 사이에 있을때 흑돌로 바꿔줘야하므로 일단 리스트에 추가해놈
#                         if arr[x][y] == 'W':
#                             white_list.append([x, y])
#                         # 탐색 좌표에 있는 돌이 흑돌일 경우, white_list에 있는 좌표의 백돌들을 모두 흑돌로 바꿔줌
#                         if arr[x][y] == 'B':
#                             for point in white_list:
#                                 arr[point[0]][point[1]] = 'B'
#                             break
#
#         # 놓은 돌이 백돌일 경우 위와 코드 동일
#         elif arr[turn[0]-1][turn[1]-1] == 'W':
#             for j in range(8):
#                 black_list = []
#                 x = turn[0] - 1
#                 y = turn[1] - 1
#                 while 0 <= x + dy[j] < len(arr) and 0 <= y + dx[j] < len(arr):
#                     x += dy[j]
#                     y += dx[j]
#                     if arr[x][y] == 0:
#                         break
#                     if arr[x][y] == 'B':
#                         black_list.append([x, y])
#                     if arr[x][y] == 'W':
#                         for point in black_list:
#                             arr[point[0]][point[1]] = 'W'
#                         break
#     white_cnt = 0
#     # 백돌 수 카운트
#     for i in range(len(arr)):
#         for j in range(len(arr[0])):
#             if arr[i][j] == 'W':
#                 white_cnt += 1
#     #흑돌의 수 = 플레이어가 돌을 놓는 횟수 + 4(초기에 놓여있는 돌의 개수) - 백돌의 개수
#     black_cnt = M+4-white_cnt
#     print('#%d %d %d' %(t, black_cnt, white_cnt))



#함수로 써서 풀기
import sys
sys.stdin = open('sample_input(1).txt')

def oselo_game(arr, turn):
    # 놓은 돌을 기준으로 바꿔야 할거 찾아서 바꾸기.
    # 왼쪽, 오른쪽, 아래, 위, 왼쪽위 대각, 오른쪽위 대각, 왼쪽 아래 대각, 오른쪽 아래대각 순으로 탐색
    for j in range(8):
        change_list = []
        x = turn[0] - 1
        y = turn[1] - 1
        # 좌표 이동했을때, 해당 좌표가 arr 내부에 있다면 계속 그 방향으로 탐색
        while 0 <= x + dy[j] < len(arr) and 0 <= y + dx[j] < len(arr):
            x += dy[j]
            y += dx[j]
            # 흑돌, 백돌이 놓여있는 부분 이외에는 다 0이므로, 탐색하다 0을 만나면 while문 탈출 (돌과 돌사이에 빈공간이 있는 경우는 의미 없으므로)
            if arr[x][y] == 0:
                break
            # 탐색을 하는데 돌이 있다면?
            else:
                # 방금 놓은 돌과 다른 색이면, 반대로 바꿔줘야하니까 change_list에 추가해줌
                color = arr[turn[0] - 1][turn[1] - 1]
                if arr[x][y] != color:
                    change_list.append([x, y])
                # 방금 놓은돌과 같은색이면, change_list에 있는 돌들의 색깔을 바꿔줌
                else:
                    for point in change_list:
                        arr[point[0]][point[1]] = color
                    break

dx = [-1, 1, 0, 0, -1, 1, -1, 1] # 왼쪽, 오른쪽, 아래, 위, 왼쪽위 대각, 오른쪽위 대각, 왼쪽 아래 대각, 오른쪽 아래대각
dy = [0, 0, 1, -1, -1, -1, 1, 1]

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0 for i in range(N)] for i in range(N)]
    arr[N//2][N//2], arr[N//2-1][N//2-1] = 'W', 'W' # 초기 흰돌이 놓여있는 상황
    arr[N//2][N//2-1], arr[N//2-1][N//2] = 'B', 'B' # 초기 검돌이 놀여있는 상황
    for i in range(M):
        turn = list(map(int, input().split()))
        #돌 놓기
        arr[turn[0]-1][turn[1]-1] = 'B' if turn[2] == 1 else 'W'
        oselo_game(arr,turn)

    white_cnt = 0
    # 백돌 수 카운트
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 'W':
                white_cnt += 1
    #흑돌의 수 = 플레이어가 돌을 놓는 횟수 + 4(초기에 놓여있는 돌의 개수) - 백돌의 개수
    black_cnt = M+4-white_cnt
    print('#%d %d %d' %(t, black_cnt, white_cnt))