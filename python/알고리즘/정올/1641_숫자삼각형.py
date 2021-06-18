n, m = map(int,input().split())

if n > 100 or n % 2 == 0 or m <1 or m > 3:
    print("INPUT ERROR!")
else:
    if m == 1:
        k = 1
        arr = [[' '] * n for _ in range(n)]
        for i in range(n):
            if i % 2 == 0:
                for j in range(i+1):
                    arr[i][j] = k
                    k += 1
            else:
                for j in range(i,-1,-1):
                    arr[i][j] = k
                    k += 1
        for i in range(n):
            print(*arr[i])
    elif m == 2:
        k = 0
        arr = [[' '] * (2 * n - 1) for _ in range(n)]
        for i in range(n):
            for j in range(i, 2 * n - 1 - i):
                arr[i][j] = k
            k += 1
        for i in range(n):
            print(*arr[i])
    else:
        k = 1
        arr = [[' '] * (n//2 + 1) for _ in range(n)]
        for i in range(n//2 + 1):
            for j in range(i, n-i):
                arr[j][i] = k
            k += 1
        for i in range(n):
            print(*arr[i])