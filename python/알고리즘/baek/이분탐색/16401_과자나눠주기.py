# 파이썬 시간초과, 파이파이 34퍼 틀림.
from sys import stdin
input = stdin.readline

m,n = map(int,input().split())
l = list(map(int,input().split()))

l.sort(reverse=True)

bottom = 1
top = l[0]

result = 0
middle = (bottom + top) // 2
cnt = 0
for i in range(n):
    temp = l[i]
    cnt += temp//middle
    if cnt > m:
        break
if cnt >= m:
    result = max(result,middle)

while bottom < top:
    middle = (bottom + top) // 2
    if middle == 0:
        middle = top
    cnt = 0
    for i in range(n):
        temp = l[i]
        cnt += temp//middle
        if cnt > m:
            break
    if cnt >= m:
        result = max(result,middle)
        bottom = middle+1
    else:
        top = middle
print(result)
