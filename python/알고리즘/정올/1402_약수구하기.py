n, k = map(int, input().split())
x = []
for i in range(1, int(n/2)+1):
    if n % i == 0:
        x.append(i)
x.append(n)

if len(x) < k:
    print(0)
else:
    print(x[k-1])