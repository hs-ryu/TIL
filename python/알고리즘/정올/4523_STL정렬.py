n = int(input())
arr = list(map(int,input().split()))
s,e = map(int,input().split())
arr2 = arr[s:e+1]
range_arr2 = sorted(arr2)
if s == 0:
    if e == n-1:
        result = range_arr2
    else:
        result = range_arr2 + arr[e+1:]
else:
    if e == n-1:
        result = arr[:s] + range_arr2
    else:
        result = arr[:s] + range_arr2 + arr[e+1:]
print(*result)
print(*sorted(result))
    