# 그냥 q로 구현하면 시간초과

from collections import deque

n = int(input())
q = deque(range(1,n+1))

while len(q) > 1:
    q.popleft()
    if len(q) == 1:
        break
    x = q.popleft()
    q.append(x)
print(q[0])