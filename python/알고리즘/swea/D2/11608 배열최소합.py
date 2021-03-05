# 열 번호만 놓고보면
# 0, 1, 2
# 0 ,2 ,1
# 1, 0, 2
# 1, 2, 0
# 2, 0 ,1
# 2, 1 ,0
# 처럼 됨. 즉 3개에서 3개를 뽑는 순열임.
# VISIT 배열
# DFS 호출


#실패 대 실패


'''
경우의 수
0행 1행 2행
0   1   2
0   2   1
1   0   2
1   2   0
2   0   1
2   1   0

level = 행 번호....
여러개의 열 중에서 1개 선택
사용한 것에 대한 체크가 필요함.(visited 사용)

재귀 함수
DFS(level, S)  # 행번호, 지금까지의 합
종료 조건 : level이 행의 크기와 같을 때
if S > min_sum:
    return

if level >= N:
    print(sel)
    if min_sum > s:
        min_sum = s
    return


DFS 함수 호출
for x in range(N):
    if not visited[x]:
        visited[x] = 1
        sel[level] = x
        DFS(level + 1, S + data[level][x])
        sel[level] = 0
        visited[x] = 0

'''

# 다시 한번 풀어보기. 나 혼자서.

import sys
sys.stdin = open('sample_input(3).txt')

# 행
# 열을 다 다르게
def DFS(level, s):
    # 가지치기
    global minV
    if s > minV:
        return
    # base case
    if level == N:
        if s < minV:
            minV = s
        return
    # 재귀
    for i in range(N):
        if visited[i] == 0:
            sel[i] = arr[level][i]
            visited[i] = 1
            DFS(level+1, s + sel[i])
            visited[i] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    minV = 10 * N * N
    sel = [0] * N
    DFS(0,0)
    print('#%d %d' %(t,minV))















'''
# 특정 행(level)에서 사용할 열을 선택함.
# level : 행 번호
# s : 선택된 열에 있는 값의 합
def DFS_sum(level, s):
    # 가지치기
    if s > min_sum:
        return
    # 종료조건
    if level >= N:
        global min_sum
        if s < min_sum:
            min_sum = s
        return
    # DFS 호출
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            DFS_sum(level+1, s + numbers[level][i])
            visited[i] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    print(numbers)
    visited = [0]*N
    min_sum = 9876543210
    DFS_sum(0, 0)
    print('#%d %s' % (t, min_sum))
'''
