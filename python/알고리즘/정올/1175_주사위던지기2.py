
def check(k):
    if k == n:
        s = sum(arr)
        if s == m:
            print(*arr)
        return
    for i in range(1,7):
        arr[k] = i
        check(k+1)
n,m = map(int, input().split())
arr = [0] * n
check(0)