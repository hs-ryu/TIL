# 아이디어
# 각 칸에서 재귀 함수 사용해 이동한 칸 수 세기
    # N이 최대 1000, n*n 인 경우 최대 1000000칸 이동 가능
    # 가능한 재귀호출 회수
        # python3는 대략 1000
        # python3.6은 대략 2300
# 재귀함수 사용 불가!
# (단, 주어진 입력데이터는 이동한 방이 최대 2200이고, pypy이므로 재귀로도 가능함.)

# 각 칸에서 단순 반복으로 갈 수 있는 칸 만큼 이동해봄.
    # 제시된 테스트케이스는 통과하지만 N=1000인 경우 시간 초과.

# 효율적인 코드와는 무관하게 

# 풀이
    # N*N까지 인덱스를 가진 V배열을 만들고 0으로 초기화 한다.
    # 모든 i,j에 대해 A[i][j] 주변에 A[i][j] + 1인 방이 있는지 확인한다.
        # 해당하는 방이 있으면 v[A[i][j]]을 1로 표시한다.
    # cnt[N*N]부터 왼쪽으로 연속한 1의 개수를 확인해 가장 긴 구간을 찾는다.
    # 연속한 개수가 같으면 더 왼쪽인 구간을 선택한다.
    # 마지막 구간의 가장 왼쪽 인덱스와 구간의 길이+1을 출력한다.










import sys
sys.stdin = open('input.txt')

#상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def search(r,c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<N and 0<=nc<N:
            if arr[nr][nc] == arr[r][c] + 1:
                cnt[arr[r][c]] = 1
                return

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = [0] * (N**2+1)
    for i in range(N):
        for j in range(N):
            search(i,j)
    len_result = 0
    length = 1
    num_result = 0

    i = 1
    while i < N**2+1:
        if cnt[i]:
            length += 1
        else:
            if length > len_result:
                len_result = length
                num_result = i-length+1
            length = 1
        i += 1
    print('#%d %d %d' %(t, num_result, len_result))