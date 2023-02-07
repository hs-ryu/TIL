arr = [[1] * 31 for i in range(31)]
for i in range(31):
    for j in range(i+1):
        if j-1 >= 0 and i != j:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

r,c,w = map(int,input().split())
result = 0
for i in range(r-1,r-1+w):
    for j in range(c-1,i-r+c+1):
        # print(i,j)
        result += arr[i][j]
print(result)