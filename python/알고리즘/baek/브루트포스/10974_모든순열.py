# 너무 쉽다. 순열 재귀문제.
def search(level, arr):
    if level == n:
        print(*arr)
        return
    for i in range(n):
        if visited[i] == 0:
            arr.append(nums[i])
            visited[i] = 1
            search(level+1, arr)
            arr.pop(-1)
            visited[i] = 0

n = int(input())
visited = [0] * n
nums = [(i+1) for i in range(n)]
search(0,[])