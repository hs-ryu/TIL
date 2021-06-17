n = int(input())
if n > 100 or n % 2 == 0:
    print('INPUT ERROR!')
else:
    arr = [[' '] * (n//2+n)for _ in range(n)]
    k = 1
    l = (n//2+n)-3
    for i in range(n//2+1):

        for j in range(i,k):
            arr[i][j] = '*'
            if i != n//2:
                arr[n-i-1][j] = '*'
        k += 3
    for i in range(n):
        print(''.join(arr[i]))

        # if i <= n//2:
        #     for j in range(i,k):
        #         arr[i][j] = '*'
        #     k += 3
        # else:
        #     for j in range(i,)