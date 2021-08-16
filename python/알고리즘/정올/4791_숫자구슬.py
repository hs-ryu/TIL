def check(t):
    total = 0
    cnt = 1
    for i in range(n):
        total += arr[i]
        if total > t:
            cnt += 1
            total = arr[i]
    return cnt <= m

n, m = map(int,input().split())
arr = list(map(int,input().split()))
s = max(arr)
e = sum(arr)

# s = 9
# e = 44

while s <= e:
    mid = (s+e)//2
    # mid = 26
    if check(mid):
        e = mid-1
    else:
        s = mid+1
print(s)

