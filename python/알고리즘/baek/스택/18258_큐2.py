# 시간초과...
# sys.stdin.readline 쓰니까 시간초과 안나네. 어휴 백준 진짜 
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
q = deque([])
for _ in range(n):
    command = input().split()
    if command[0] == "push":
        q.append(int(command[1]))
    elif command[0] == "pop":
        if q:
            x = q.popleft()
            print(x)
        else:
            print(-1)
    elif command[0] == "size":
        print(len(q))
    elif command[0] == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif command[0] == "back":
        if q:
            print(q[-1])
        else:
            print(-1)