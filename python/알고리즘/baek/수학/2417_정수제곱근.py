import math
n = int(input())
# k = math.isqrt(n)
# print(k)

l = 0
r = n
while l < r:
    m = (l + r) // 2
    if m ** 2 < n:
        l = m+1
    else:
        r = m
print(l) 