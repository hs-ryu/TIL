m = int(input())
n = int(input())

def prime(n):
    if n < 2:
        return False
    root = n ** (0.5)
    for i in range(2, int(root) + 1):
        if n % i == 0:
            return False
    return True


max_sum = 0
min_sum = 0
for num in range(m,n+1):
    result = prime(num)
    if result:
        max_sum += num
        if min_sum == 0:
            min_sum += num
if min_sum == 0:
    print(-1)
else:
    print(max_sum)
    print(min_sum)