def get_gcd(x,y):
    r = 0
    while y != 0:
        r = x % y
        x = y
        y = r
    return x
n = int(input())
k = list(map(int,input().split()))
gcd = lcm = k[0]
for i in range(n):
    gcd = get_gcd(gcd, k[i])
    lcm = int(lcm / get_gcd(lcm, k[i]) * k[i])
print(gcd, lcm)