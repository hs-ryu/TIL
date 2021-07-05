n = int(input())
arr = list(map(int,input().split()))

result = 0
total = 0
for i in range(n):
    num = arr[i]
    if total > 0:
        total += num
    else:
        total = num
    if result < total:
        result = total
print(result)