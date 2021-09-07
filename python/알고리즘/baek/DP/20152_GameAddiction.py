import math
n, m = map(int, input().split())
n -= m
n = abs(n)
m = math.factorial
print(m(2 * n) // m(n) // m(n) // (n+1))