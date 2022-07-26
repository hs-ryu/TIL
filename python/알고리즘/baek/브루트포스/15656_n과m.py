def search(level, arr):
    if level == m:
        print(*arr)
        return

    for i in range(n):
        arr.append(nums[i])
        search(level+1, arr)
        arr.pop(-1)


n,m = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
search(0,[])