n = int(input())
arr = list(map(int, input().split()))
m = int(input())

yaksoo = 0
baesoo = 0
for num in arr:
    if m % num == 0:
        yaksoo += num
    if num % m == 0:
        baesoo += num
print(yaksoo)
print(baesoo)
    