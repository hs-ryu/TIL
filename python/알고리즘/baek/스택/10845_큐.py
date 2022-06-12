from collections import deque
from sys import stdin
input = stdin.readline
n = int(input())
q = deque()
for _ in range(n):
    command = list(input().split())
    if command[0] == "push":
        q.append(int(command[1]))
    elif command[0] == "pop":
        if len(q):
            x = q.popleft()
            print(x)
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == "empty":
        if len(q):
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if len(q):
            print(q[0])
        else:
            print(-1)
    else:
        if len(q):
            print(q[-1])
        else:
            print(-1)