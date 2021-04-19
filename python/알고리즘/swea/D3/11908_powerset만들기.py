import sys
sys.stdin = open('ex02_input.txt')


# 일반 조합으로 풀기
def powerset(s, k):
    global cnt
    # 이미 합이 M보다 크다면 더이상 검색 필요 X
    if s > M:
        return
    # 합이 M과 같다면 cnt 증가
    if s == M:
        cnt += 1
        return
    # 고른 개수가 N개 이상 되면? 리턴
    if k >= N:
        return
    powerset(s+arr[k], k+1)
    powerset(s, k+1)


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    powerset(0, 0)
    print("#%d %d" %(t, cnt))




# 비트 연산으로 풀기
def powerset():
    global cnt
    # 2 ^ N번 반복
    for i in range(1<<N):
        x = 0
        # N번 반복
        for j in range(N):
            if i & (1<<j):
                x += arr[j]
    if x == M:
        cnt += 1

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    powerset()
    print("#%d %d" %(t, cnt))




# # 교수님 풀이

# def func(level, c_sum):
#     # 남아있는 애들을 다 더해줘도 M이 안될땐 생각할 필요도 없다.
#     # 단, 이때는 새로운 배열을 하나 선언해서 사용해야함.
#     if c_su > M or c_sum + remain[level] < M:
#         return
#     if level >= N:
#         print(''.join(str(a[x]) for x in range(N) if status[x]))
#         return
    
#     status[level] = 1
#     if      : func(level+1, c_sum + a[level])
#     status[level] = 0
#     if      : func(level+1, c_sum)




# # 순열 교수님 풀이

# visit = [0] * N # 사용했는지 사용하지 않았는지
# status = [0] * N  # 현재 순열의 상태
# def func(level):
#     if level >= N:
#         print(''.join(str(a[x]) for x in range(N) if status[x]))
#         return

#     for x in range(N):
#         if visit[x] == 1:
#             continue
#         visit[x] = 1
#         status[level] = a[x]
#         func(level+1)
#         status[level] = 0
#         visit[x] = 0
