n = int(input())
x = sum(range(1,n+1))

a = ''
b = 0
c = 65
while b < x:
    if c == 91:
        c = 65
    a += chr(c)
    b += 1
    c += 1



arr = [[' '] * n for _ in range(n)]
k = 0
for i in range(n):
    m = n-1
    for j in range(i,n):
        arr[j][m] = a[k]
        m -= 1
        k += 1
for i in range(n):
    print(*arr[i])

