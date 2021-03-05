import sys
sys.stdin = open('sample_input (1).txt')


# 1. 누적...?,
# 2. 행마다 체크.
# 3.

# 3.


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    russia = [list(input()) for _ in range(N)]
    print(russia)

    #각 색깔
    white = [0] * N
    blue = [0] * N
    red = [0] * N

    #다른색깔 세기
    for i in range(N):
        for j in range(M):
            if russia[i][j] != 'W':
                white[i] += 1
            if russia[i][j] != 'B':
                blue[i] += 1
            if russia[i][j] != 'R':
                red[i] += 1

    for i in range(1, N):
        white[i] += white[i-1]
        blue[i] += blue[i-1]
        red[i] += red[i-1]

    ans = 987654321
    #이부분 개어렵다.
    for i in range(N-2):
        for j in range(i+1, N-1):
            w_cnt = white[i]
            b_cnt = blue[j] - blue[i]
            r_cnt = red[N-1] - red[j]

            if ans > w_cnt + b_cnt + r_cnt:
                ans = w_cnt + b_cnt + r_cnt
    print("#%d %d" % (t, ans))



#
#
# # 풀이
# #중복순열!!!
#
# def perm(level, s):
#     # 유망성 검사. 아래의 조건문에 걸리게 되면 이후 작업은 의미가 없음.
#     global ans
#     if s > N:
#         return
#
#     if level == 3:
#         if s == N:
#             cnt = 0
#
#             st = sel[0]
#             st2 = st + sel[1]
#
#             # 흰색 칠하기
#             for i in flag[:st]:
#                 for j in i:
#                     if j != 'W':
#                         cnt += 1
#
#             # 파란색 칠하기
#             for i in flag[st:st2]:
#                 for j in range(i):
#                     if j != 'B':
#                         cnt += 1
#
#             for i in flag[st2:]:
#                 for j in range(i):
#                     if j != 'R':
#                         cnt += 1
#
#             if ans > cnt:
#                 ans = cnt
#         return
#
#     # 중복 순열 살짝 응용
#     for i in range(1, N-1):
#         sel[level] = i
#         perm(level + 1, s + i)
#
# T = int(input())
# for t in range(1, T+1):
#     N, M = map(int, input().split())  # N행, M열
#
#     flag = [list(input()) for _ in range(N)]
#     sel = [0] * 3
#     ans = 987654321
#
#     # 앞에는 idx, 뒤에는 중간 합
#     perm(0, 0)
#
#
#
# #############################################################
# #풀이 2
# #누적합
#
# T = int(input())
# for t in range(1, T+1):
#     N, M = map(int, input().split())  # N행, M열
#
#     flag = [list(input()) for _ in range(N)]
#
#     W = [0] * N
#     B = [0] * N
#     R = [0] * N
#
#     # 행을 보면서 나와 다른 색깔의 개수를 카운팅
#     for i in range(N):
#         for j in range(M):
#             if flag[i][j] != 'W':
#                 W[i] += 1
#             if flag[i][j] != 'B':
#                 B[i] += 1
#             if flag[i][j] != 'R':
#                 R[i] += 1
#
#     # 누적 시키자
#     for i in range(1, N):
#         W[i] += W[i-1]
#         B[i] += B[i-1]
#         R[i] += R[i-1]
#
#     ans = 987654321
#
#     # 각각의 색 별로 한 줄 이상은 확보해야하니까 N-2까지
#     for i in range(N-2):
#         for j in range(i+1, N-1):
#             w_cnt = W[i]
#             b_cnt = B[j] - B[i]
#             r_cnt = R[N-1] - R[j]
#
#             if ans > w_cnt + b_cnt + r_cnt:
#                 ans = w_cnt + b_cnt + r_cnt
#     print("#%d %d" % (t, ans))
#
#
