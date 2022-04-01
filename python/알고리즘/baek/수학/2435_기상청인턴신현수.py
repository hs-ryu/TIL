n,k = map(int,input().split())
c = list(map(int,input().split()))

i = 0
max_v = -100000
while i+k <= n:
    temp = sum(c[i:i+k])
    if temp > max_v:
        max_v = temp
    i += 1
print(max_v)