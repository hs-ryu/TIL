n = int(input())

arr = [[0] * n for _ in range(n)]

a = 0
b = 65
c = ''
while a < n * n:
    if b == 91:
        b = 65
    c += chr(b)
    a += 1
    b += 1

k = 0
for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        arr[j][i] = c[k]
        k += 1

for i in range(n):
    print(*arr[i])