n = int(input())

a = ''
b = 0
c = 65

while b < n * n:
    if c == 91:
        c = 65
    a += chr(c)
    b += 1
    c += 1

arr = [[0] * n for _ in range(n)]
k = 0
for i in range(n):
    if i % 2:
        for j in range(n-1,-1,-1):
            arr[j][i] = a[k]
            k += 1
    else:
        for j in range(n):
            arr[j][i] = a[k]
            k += 1
for i in range(n):
    print(*arr[i])