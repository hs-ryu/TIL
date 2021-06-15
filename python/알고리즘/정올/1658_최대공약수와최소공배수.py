def gcd_get(x,y):
    r = 0
    while y != 0:
        r = x % y
        x = y
        y = r
    return x

n, m = map(int,input().split())

if n > m:
    gcd = gcd_get(n,m)
    
else:
    gcd = gcd_get(m,n)
lcm = int(m * n / gcd)
print(gcd)
print(lcm)