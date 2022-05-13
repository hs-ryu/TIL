# 파이썬 시간초과, 파이파이 34퍼 틀림.

m,n = map(int,input().split())
l = list(map(int,input().split()))

l.sort(reverse=True)

bottom = 0
top = l[0]

result = 0
while bottom < top:
    
    middle = (bottom + top) // 2
    if middle == 0:
        middle = top
    
    cnt = 0
    for i in range(n):
        temp = l[i]
        while temp >= middle and cnt < m:
            temp -= middle
            cnt += 1
        if cnt > m:
            break
    # print(middle, cnt)
    if cnt >= m:
        result = middle
        bottom = middle+1
    else:
        top = middle
print(result)   
    