n = int(input())
m = int(input())
metal = list(map(int,input().split()))
metal.sort()

l = 0
r = len(metal)-1
result = 0
while l < r:
    a = metal[l]
    b = metal[r]
    if a + b < m:
        l += 1
    elif a + b > m:
        r -= 1
    else:
        l += 1
        r -= 1
        result += 1
print(result)