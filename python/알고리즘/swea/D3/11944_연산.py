
import sys
sys.stdin = open('5247_input.txt')

# 디큐 쓰기
# from collections import deque
# dx = [1, -1, -10, 2]

# def calc():
#     cnt = [0] * 1000001
#     q = deque()
#     q.append(N)

#     while q:
#         temp = q.popleft()
#         for i in range(4):
#             if i == 3:
#                 x = temp * dx[i]
#             else:
#                 x = temp + dx[i]
#             if 0 <= x < 1000001 and cnt[x] == 0:
#                 cnt[x] = cnt[temp] + 1
#                 if x == M:
#                     return cnt[x]
#                 q.append(x)
    

# T = int(input())
# for t in range(1, T+1):
#     N, M = map(int, input().split())
#     result = calc()
#     print('#%d %d' %(t, result))


# 디큐 안쓰기
dx = [1, -1, -10, 2]

def calc():
    cnt = [0] * 1000001
    q = [N]
    front = 0
    while q:
        temp = q[front]
        front += 1
        for i in range(4):
            if i == 3:
                x = temp * dx[i]
            else:
                x = temp + dx[i]
            if 0 <= x < 1000001 and cnt[x] == 0:
                cnt[x] = cnt[temp] + 1
                if x == M:
                    return cnt[x]
                q.append(x)
    

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    result = calc()
    print('#%d %d' %(t, result))
