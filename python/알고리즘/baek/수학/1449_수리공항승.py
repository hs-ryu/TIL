n,l = map(int,input().split())

points = list(map(int,input().split()))

points.sort()

clears = [0] * n
result = 0
for i in range(n):
    if clears[i] == 0:
        j = i+1
        result += 1
        while j < n:
            if points[i] + l > points[j]:
                clears[j] = 1
            else:
                break 
            j += 1
print(result)