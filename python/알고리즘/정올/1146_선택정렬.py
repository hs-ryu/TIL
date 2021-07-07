n = int(input())
nums = list(map(int,input().split()))

for i in range(len(nums)-1):
    min_v = nums[i]
    min_index = i
    for j in range(i+1, len(nums)):
        if nums[j] < min_v:
            min_v = nums[j]
            min_index = j
    nums[i], nums[min_index] = nums[min_index], nums[i]
    print(*nums)