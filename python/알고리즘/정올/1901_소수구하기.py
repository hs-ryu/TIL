def prime(n):
    if n < 2:
        return False
    root = int(n ** 0.5)
    for i in range(2, root+1):
        if n % i == 0:
            return False
    return True


n = int(input())
for i in range(n):
    m = int(input())
    
    if prime(m):
        print(m)
    else:
        k = 1
        flag = 0
        x = []
        while not flag:
            if prime(m-k):
                flag = 1
                x.append(m-k)
            if prime(m+k):
                flag = 1
                x.append(m+k)
            k += 1
        print(*x)
