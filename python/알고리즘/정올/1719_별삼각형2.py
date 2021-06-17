n, m = map(int, input().split())



if n > 100 or n % 2 == 0 or m < 1 or m > 4:
    print("INPUT ERROR!")
else:
    if m == 1:
        arr = [[' '] * (n//2+1) for _ in range(n)]
        for i in range(n//2, -1, -1):
            for j in range(i,n-i):
                arr[j][i] = '*'
        for i in range(n):
            print(''.join(arr[i]))
    elif m == 2:
        arr = [[' '] * (n//2+1) for _ in range(n)]
        k = 0
        for i in range(n//2, -1, -1):
            for j in range(k,n-k):
                arr[j][i] = '*'
            k += 1
        for i in range(n):
            print(''.join(arr[i]))
        
    elif m == 3:
        arr = [[' '] * n for _ in range(n)]
        for i in range(n):
            if i <= n//2:
                for j in range(i, n-i):
                    arr[i][j] = '*'
            else:
                for j in range(n-i-1, i+1):
                    arr[i][j] = '*'
        for i in range(n):
            print(''.join(arr[i]))
    else:
        arr = [[' '] * n for _ in range(n)]
        for i in range(n):
            if i <= n//2:
                for j in range(i,n//2+1):
                    arr[i][j] = '*'
            else:
                for j in range(n//2,i+1):
                    arr[i][j] = '*'
        for i in range(n):
            print(''.join(arr[i]))