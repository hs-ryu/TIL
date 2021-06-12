n = int(input())

if n % 2 == 0 or n > 100 or n < 1:
    print("INPUT ERROR")
else:
    arr = [[' '] * n for _ in range(n)]
    k = 65
    for i in range(n//2, -1 , -1):
        for j in range(i, n-i):
            if k >= 91:
                k = 65
            arr[j][i] = chr(k)
            k += 1

    for i in range(n):
        print(*arr[i])
