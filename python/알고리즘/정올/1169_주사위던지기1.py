n, m = map(int, input().split())

def m1(k):
    if k == n:
        print(*arr)
        return
    for i in range(1,7):
        arr[k] = i
        m1(k+1)

def m2(k):
    if k == n:
        print(*arr)
        return
    x = arr[k-1] if k > 0 else 1
    for i in range(x, 7):
        arr[k] = i
        m2(k+1)

def m3(k):
    if k == n:
        for i in range(n):
            if arr.count(arr[i]) > 1:
                return
        print(*arr)
        return

    for i in range(1,7):
        arr[k] = i
        m3(k+1)
        
if m == 1:
    arr = [0] * n
    m1(0)
elif m == 2:
    arr = [0] * n
    arr[0] = 1
    m2(0)
else:
    arr = [0] * n
    m3(0)