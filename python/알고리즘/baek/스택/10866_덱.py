from collections import deque
from sys import stdin
input = stdin.readline
q = deque()
n = int(input())

for _ in range(n):
    comand = list(input().split())
    if comand[0] == "push_front":
        q.insert(0,int(comand[1]))
    elif comand[0] == "push_back":
        q.append(int(comand[1]))
    elif comand[0] == "pop_front":
        if len(q):
            k = q.popleft()
            print(k)
        else:
            print(-1)
    elif comand[0] == "pop_back":
        print(q.pop() if len(q) else -1)
    elif comand[0] == "size":
        print(len(q))
    elif comand[0] == "empty":
        print(0 if len(q) else 1)
    elif comand[0] == "front":
        print(q[0] if len(q) else -1)
    elif comand[0] == "back":
        print(q[-1] if len(q) else -1)