import sys
sys.stdin = open('input2.txt')
from pprint import pprint


# 1. 배열 순회하면서 시작점 찾기.(0이 아닌점)   ok
# 2. 찾으면 BFS에 시작점으로 돌려줌. 반복문으로 돌려줘야할듯
# 3. 좌표 순환하면서 0으로 바꿔줌. 바로 좌표에서 바꿔주자. OR visited 배열에 채크해줌
# 4. 마지막으로 바꾼 점을 체크. 마지막점 - 시작점 + 1 => 행,열 길이  good!
# 5. 정렬.
#     - 크기가 작은 순서대로 출력.
#     - 크기가 같을 경우 행의 크기가 작은 순으로 출력.


#굳굳 너무 굳

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(sr, sc):
    Q = [[sr, sc]]
    arr[sr][sc] = 0

    while Q:
        r, c = Q.pop(0)
        for i in range(4):
            cr = r + dr[i]
            cc = c + dc[i]
            if 0<=cr<n and 0<=cc<n and arr[cr][cc]:
                arr[cr][cc] = 0
                Q.append([cr, cc])
    return cr - sr + 1, cc - sc




T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                sr, sc = i, j
                result.append(list(BFS(sr, sc)))
    cnt = len(result)
    result.sort(key = lambda x:(x[0]*x[1], x[0]))
    res = ''
    for i in result:
        print(i)
        res += ' '.join(map(str, i)) + ' '
    print('#%d %d %s' % (t, cnt, res.rstrip()))












#
#
# # 풀이
# # 사각형의 크기를 찾아주는 함수
# def search_size(r, c):
#     r_cnt = 0
#     c_cnt = 0
#
#     # 행의 길이를 찾는
#     for i in range(r, N):
#         if arr[i][c] != 0:
#             r_cnt += 1
#         else:
#             break
#
#     # 열의 길이를 찾는
#     for i in range(c, N):
#         if arr[r][i] != 0:
#             c_cnt += 1
#         else:
#             break
#
#     ans.append([r_cnt, c_cnt, r_cnt * c_cnt])
#     init(r, c, r_cnt, c_cnt)
#
#
# # 화학 물질들을 빈 용기로 반환
# def init(r, c, r_cnt, c_cnt):
#     for i in range(r, r+r_cnt):
#         for j in range(c, c+c_cnt):
#             arr[i][j] = 0
#
#
# def counting_sort(idx):
#     cnt = [0] * 10001    # 배열 크기가 100 * 100이니까
#     sort_ans = [0] * len(ans)
#
#     # 1.카운팅 하는 과정
#     for i in range(len(ans)):
#         cnt[ans[i][idx]] += 1
#
#     # 2.누적하는 과정
#     for i in range(1, len(cnt)):
#         cnt[i] += cnt[i-1]
#
#     # 3.정렬하여 넣는 과정
#     for i in range(len(ans)-1, -1, -1):
#         sort_ans[cnt[ans[i][idx]] - 1] = ans[i]
#         cnt[ans[i][idx]] -= 1
#
#     return sort_ans
#
#
# T = int(input())
# for t in range(1, T+1):
#     N = int(input())    # 2차원 리스트의 크기 100 이하
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     ans = []
#
#     # 행 우선순회 방식으로 순회하면서 사각형의 시작좌표를 구한다.
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] != 0:
#                 search_size(i, j)
#
#     ans = counting_sort(0)  # 행을 기준으로 정렬
#     ans = counting_sort(2)  # 행렬의 크기로 다시한번 정렬하자
#
#     print("#%d %d" % (t, len(ans)), end=" ")
#     print(*ans)
#
#
#
#
#
#
#
#
#
# # 풀이 2
# T = int(input())
# for t in range(1, T+1):
#     N = int(input())    # 2차원 리스트의 크기 100 이하
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     ans = []
#
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] != 0:
#                 r, c = i, j
#                 # 범위를 앞에 위치
#                 while r < N and arr[r][j] != 0:
#                     r += 1
#                 while c < N and arr[i][c] != 0:
#                     c += 1
#                 ans.append([r-i, c-j])
#
#                 # 초기화 하는 작업
#                 for a in range(i, r):
#                     for b in range(j, c):
#                         arr[a][b] = 0
#
#
#     # lambda x : (x[0], x[1])      ->      1차 : x[0]를,  2차 : x[1]
#     ans.sort(key = lambda x : (x[0]*x[1], x[0]))
#     print(*ans)