n = int(input())
a = list(map(int,input().split()))
x = int(input())
a.sort()

l = 0
r = len(a)-1

result = 0
while l < r:
    if a[l] + a[r] > x:
        r -= 1
    elif a[l] + a[r] < x:
        l += 1
    elif a[l] + a[r] == x:
        result += 1
        l += 1
        r -= 1
print(result)
