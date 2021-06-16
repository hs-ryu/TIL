n, m = map(int, input().split())

if n > 100 or m < 1 or m > 3:
    print('INPUT ERROR!')

else:
    if m == 1:
        for i in range(n):
            print('*' * (i+1))
    elif m == 2:
        for i in range(n,-1,-1):
            print('*' * i)
    else:
        k = 1
        arr = [' '] * (2 * n - 1)
        for i in range(n):
            arr[n-i-1:n+i-1] = '*' * k
            k += 2
            print(''.join(arr))
