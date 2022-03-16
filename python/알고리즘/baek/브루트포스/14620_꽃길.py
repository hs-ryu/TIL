n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]


from pprint import pprint

visited = [[0] * n for _ in range(n)]
min_value = 100 * 200
for i in range(1,n-1):
    for j in range(1,n-1):
        temp_value = 0
        visited[i][j] = 1
        visited[i-1][j] = 1
        visited[i][j-1] = 1
        visited[i+1][j] = 1
        visited[i][j+1] = 1
        temp_value += arr[i][j]
        temp_value += arr[i-1][j]
        temp_value += arr[i][j-1]
        temp_value += arr[i+1][j]
        temp_value += arr[i][j+1]
        # pprint(visited)
        for k in range(1,n-1):
            for l in range(1,n-1):
                if visited[k][l] or visited[k-1][l] or visited[k][l-1] or visited[k+1][l] or visited[k][l+1]:
                    continue
                visited[k][l] = 1
                visited[k-1][l] = 1
                visited[k][l-1] = 1
                visited[k+1][l] = 1
                visited[k][l+1] = 1
                temp_value += arr[k][l]
                temp_value += arr[k-1][l]
                temp_value += arr[k][l-1]
                temp_value += arr[k+1][l]
                temp_value += arr[k][l+1]
                for m in range(1,n-1):
                    for o in range(1,n-1):
                        if visited[m][o] or visited[m-1][o] or visited[m][o-1] or visited[m+1][o] or visited[m][o+1]:
                            continue
                        temp_value += arr[m][o]
                        temp_value += arr[m-1][o]
                        temp_value += arr[m][o-1]
                        temp_value += arr[m+1][o]
                        temp_value += arr[m][o+1]
                        if temp_value < min_value:
                            min_value = temp_value
                        temp_value -= arr[m][o]
                        temp_value -= arr[m-1][o]
                        temp_value -= arr[m][o-1]
                        temp_value -= arr[m+1][o]
                        temp_value -= arr[m][o+1]
                temp_value -= arr[k][l]
                temp_value -= arr[k-1][l]
                temp_value -= arr[k][l-1]
                temp_value -= arr[k+1][l]
                temp_value -= arr[k][l+1]
                visited[k][l] = 0
                visited[k-1][l] = 0
                visited[k][l-1] = 0
                visited[k+1][l] = 0
                visited[k][l+1] = 0
        visited[i][j] = 0
        visited[i-1][j] = 0
        visited[i][j-1] = 0
        visited[i+1][j] = 0
        visited[i][j+1] = 0
        
print(min_value)