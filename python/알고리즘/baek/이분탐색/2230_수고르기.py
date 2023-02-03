from sys import stdin
input = stdin.readline

n,m = map(int,input().split())
a = [int(input()) for _ in range(n)]
a.sort()
l = 0
r = 1
# 하,, 여기 result의 초기값때매 계속 틀렸네.
# 단순히 배열에서 가장 큰 값이 아니라, m의 최대값으로 result 값을 초기화시켜줘야한다.
result = 2000000001
flag = 0
while l < n and r < n:
    x = a[r] - a[l]
    if x == m:
        flag=1
        break
    if x < m:
        r += 1
    else:
        l += 1
        result = min(result,x)
if flag:
    print(m)
else:
    print(result)