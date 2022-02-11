

# 0  => 1
# 0 1 => 2
# 01 10 => 4
# 0110 1001 => 8
# 01101001 10010110 => 16
# 2의 제곱만큼.

# 1 = 0 2^0
# 2 = 1 2^1
# 3 = 1
# 4 = 0 2^2
# 5 = 1
# 6 = 0
# 7 = 0
# 8 = 1 2^3
# 9 = 1
# 10 = 0
# 11 = 0
# 12 = 1
# 13 = 0
# 14 = 1
# 15 = 1
# 16 = 0 2^4

# x(1) = 0
# x(2n-1) = x(n)
# x(2n) = 1-x(n)

# ??
def search(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif not n % 2:
        return search(n//2)
    elif n % 2:
        return 1-search(n//2)

k = int(input())
result = search(k-1)
print(result)