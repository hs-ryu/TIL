n = int(input())

k = []
geun = int(n**(0.5))
for i in range(1, geun+1):
    if n % i == 0:
        k.append(i)
        if (n/i != i):
            k.append(n//i)
k.sort()
print(*k)
