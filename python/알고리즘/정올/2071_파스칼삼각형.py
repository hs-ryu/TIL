n,m = map(int, input())


arr = [[' '] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        arr[i][j] = 1
for i in range(2,n):
    for j in range(1,i):
        arr[i][j] = arr[i-1][j] + arr[i-1][j-1]
if m == 1:
    for i in range(n):
        print(*arr[i])
elif m == 2:
    for i in range(n-1, -1, -1):
        for j in range(n-i-1):
            print(" ", end='')
        for j in range(i, -1,-1):
            print()
