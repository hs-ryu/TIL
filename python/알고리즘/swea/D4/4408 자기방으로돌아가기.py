import sys
sys.stdin = open('sample_input.txt')

# T = int(input())
# for t in range(1, T+1):
#     room = [0] * 201
#     N = int(input())
#     for _ in range(N):
#         s, e = map(int, input().split())
#         if s > e:
#             s, e = e, s
#         if s % 2:
#             s += 1
#         if e % 2:
#             e += 1
#         for i in range(s//2, (e//2) + 1):
#             room[i] += 1
#     time = max(room)
#     print('#%d %d' %(t, time))



#성공 대 성공
T = int(input())
for t in range(1, T+1):
    N = int(input())
    #통로
    visited = [0 for _ in range(200)]

    for i in range(N):
        move = list(map(int,input().split()))
        if move[0] > move[1]:
            move[0], move[1] = move[1], move[0]
        if not move[0] % 2:
            move[0] -= 1
        if not move[1] % 2:
            move[1] -= 1
        for j in range(move[0]//2, move[1]//2 + 1):
            visited[j] += 1

    #총 이동횟수
    cnt = 0
    for i in visited:
        if cnt < i:
            cnt = i
    print('#%d %d' % (t, cnt))
