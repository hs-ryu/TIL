n = int(input())
arr = list(map(int,input().split()))
result = sorted(arr, reverse=True)
print(*result)