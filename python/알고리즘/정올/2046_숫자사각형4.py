n,m = map(int,input().split())

arr = [[] for _ in range(n)]
if m == 1:
    for i in range(n):
        for j in range(n):
            arr[i].append(i+1)
        print(*arr[i])
elif m == 2:
    for i in range(n):
        a = [j+1 for j in range(n)]
        arr[i].extend(a)
    for i in range(n):
        if i % 2:
            print(*reversed(arr[i]))
        else:
            print(*arr[i])
else:
    for i in range(n):
        a = [(j+1) * (i+1) for j in range(n)]
        
        arr[i].extend(a)
    for i in range(n):
        print(*arr[i])