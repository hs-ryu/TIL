n = int(input())
province = list(map(int,input().split()))
m = int(input())

# 이분탐색!
l = 0
r = max(province) + 1
result = 0
while l < r:
    # print(l,r)
    middle = (l+r) // 2
    total = 0 
    for i in range(n):
        if province[i] > middle:
            total += middle
        else:
            total += province[i]
    if total > m:
        r = middle
    else:
        l = middle + 1
        result = max(result,  middle)
print(result)

