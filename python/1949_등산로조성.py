'''
등산로를 조성하려고 한다.

등산로를 만들기 위한 부지는 N * N 크기를 가지고 있으며, 이곳에 최대한 긴 등산로를 만들 계획이다.

등산로 부지는 아래 [Fig. 1]과 같이 숫자가 표시된 지도로 주어지며, 각 숫자는 지형의 높이를 나타낸다.

등산로를 만드는 규칙은 다음과 같다.

   ① 등산로는 가장 높은 봉우리에서 시작해야 한다.

   ② 등산로는 산으로 올라갈 수 있도록 반드시 높은 지형에서 낮은 지형으로 가로 또는 세로 방향으로 연결이 되어야 한다.
       즉, 높이가 같은 곳 혹은 낮은 지형이나, 대각선 방향의 연결은 불가능하다.

   ③ 긴 등산로를 만들기 위해 딱 한 곳을 정해서 최대 K 깊이만큼 지형을 깎는 공사를 할 수 있다.

N * N 크기의 지도가 주어지고, 최대 공사 가능 깊이 K가 주어진다.

이때 만들 수 있는 가장 긴 등산로를 찾아 그 길이를 출력하는 프로그램을 작성하라.


[예시]

위 [Fig. 1]과 같이 N = 5인 지도가 주어진 경우를 살펴보자.

가장 높은 봉우리는 높이가 9로 표시된 세 군데이다.

이 세 곳에서 출발하는 가장 긴 등산로 중 하나는 아래 [Fig. 2]와 같고, 이 때 길이는 5가 된다.
 
 

만약 최대 공사 가능 깊이 K = 1로 주어질 경우,

아래 [Fig. 3]과 같이 빨간색 부분의 높이를 9에서 8로 깎으면 길이가 6인 등산로를 만들 수 있다.
 


이 예에서 만들 수 있는 가장 긴 등산로는 위와 같으며, 출력할 정답은 6이 된다.


[제약 사항]

1. 시간 제한 : 최대 51개 테스트 케이스를 모두 통과하는 데 C/C++/Java 모두 3초

2. 지도의 한 변의 길이 N은 3 이상 8 이하의 정수이다. (3 ≤ N ≤ 8)

3. 최대 공사 가능 깊이 K는 1 이상 5 이하의 정수이다. (1 ≤ K ≤ 5)

4. 지도에 나타나는 지형의 높이는 1 이상 20 이하의 정수이다.

5. 지도에서 가장 높은 봉우리는 최대 5개이다.

6. 지형은 정수 단위로만 깎을 수 있다.

7. 필요한 경우 지형을 깎아 높이를 1보다 작게 만드는 것도 가능하다.

[입력]

입력의 맨 첫 줄에는 총 테스트 케이스의 개수 T가 주어지고, 그 다음 줄부터 T개의 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 지도의 한 변의 길이 N, 최대 공사 가능 깊이 K가 차례로 주어진다.

그 다음 N개의 줄에는 N * N 크기의 지도 정보가 주어진다.

[출력]

테스트 케이스 개수만큼 T개의 줄에 각각의 테스트 케이스에 대한 답을 출력한다.

각 줄은 "#t"로 시작하고 공백을 하나 둔 다음 정답을 출력한다. (t는 1부터 시작하는 테스트 케이스의 번호이다)

출력해야 할 정답은 만들 수 있는 가장 긴 등산로의 길이이다.
'''

import sys
sys.stdin = open('1949.txt')


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def DFS(r,c):
    global cut, max_length

    for i in range(4):
        cr = r + dr[i]
        cc = c + dc[i]
        if 0 <= cr < N and 0 <= cc < N:
            if visited[cr][cc] == 0:
                if jido[cr][cc] < jido[r][c]:
                    visited[cr][cc] = visited[r][c] + 1
                    DFS(cr, cc)
                    visited[cr][cc] = 0
                elif cut and jido[cr][cc] - jido[r][c] < K:
                    now = jido[cr][cc]
                    jido[cr][cc] = jido[r][c] - 1
                    visited[cr][cc] = visited[r][c] + 1
                    cut = 0
                    DFS(cr, cc)
                    jido[cr][cc] = now
                    visited[cr][cc] = 0
                    cut = 1
                else:
                    if visited[r][c] > max_length:
                        max_length = visited[r][c]

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    maxV = 0
    jido = []
    for i in range(N):
        jido_r = list(map(int, input().split()))
        maxV = max(maxV, max(jido_r))
        jido.append(jido_r)
    highst = []
    for i in range(N):
        for j in range(N):
            if jido[i][j] == maxV:
                highst.append([i,j])
    visited = [[0] * N for _ in range(N)]
    cut = 1
    max_length = 0
    for i,j in highst:
        visited[i][j] = 1
        DFS(i,j)
        visited[i][j] = 0

    print('#%d %d' % (t, max_length))




















# 아이디어
# 가장 높은 봉우리 높이 h를 찾는다
# 높이가 h인 모든 칸에서 시작해본다
# 현재 칸에 인접한 낮은 칸으로 이동한다
# 낮지 않은 칸은, 높이차이가 K보다 작고 깎는 획수가 남아있으면 이동한다.
#     이미 등산로에 포함된 칸을 깎이 않도록 한다.
#     깍은 칸 방향 탐색 후 다른 방향을 탐색할 때 원래 높이를 복원한다.
# 각 칸에 들어갈 때 마다, 가장 긴 등산로와 비교해 최대 길이를 갱신한다.


#재귀 사용(DFS)
#재귀 끝나면 visited 다시 0으로 변환