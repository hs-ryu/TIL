n = int(input())

arr = [[] for _ in range(n)]
for i in range(n):
    for j in range(1,n+1):
        arr[i].append((n*i)+j)

result = list(zip(*arr))
for a in result:
    print(*a)
