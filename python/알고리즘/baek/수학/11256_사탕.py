t = int(input())
for _ in range(t):
    j,n = map(int,input().split())
    arr = []
    for i in range(n):
        r,c = map(int,input().split())
        arr.append(r*c)
    arr.sort()
    
    total = j
    result = 0
    while len(arr) > 0:
        if total <= 0:
            break
        now = arr.pop(-1)
        total -= now
        result += 1
    print(result)