def prime(n):
    if n < 2:
        return False
    root = n ** (0.5)
    for i in range(2, int(root)+1):
        if n % i == 0:
            return False
    return True

def composite(n):
    if n < 2:
        return False
    root = n ** (0.5)
    for i in range(2, int(root) + 1):
        if n % i == 0:
            return True
    return False
    

nums = list(map(int, input().split()))

for num in nums:
    result1 = prime(num)
    result2 = composite(num)
    if result1:
        print("prime number")
    elif result2:
        print("composite number")
    else:
        print("number one")