def calc(num,arr):
    s = num * n % p
    if s in arr:
        print(len(arr)-arr.index(s))
        return
    arr.append(s)
    calc(s,arr)

n, p = map(int,input().split())
calc(n,[n])