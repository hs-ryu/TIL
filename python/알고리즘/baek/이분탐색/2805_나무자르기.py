# 시간초과, pypy 통과

n,m = map(int,input().split())

trees = list(map(int,input().split()))

l = 0
r = max(trees)
while l < r:
    middle = (l + r)//2
    total = 0
    for i in range(n):
        if trees[i] > middle:
            total += trees[i] - middle
    if total < m:
        r = middle
    else:
        l = middle + 1
print(l-1)
