n = int(input())
nums = list(map(int,input().split()))

# 커지는 수열 체크
cnt = 1
max_cnt = 1
for i in range(1,n):
    if nums[i] >= nums[i-1]:
        cnt += 1
    else:
        cnt = 1
    if cnt > max_cnt:
        max_cnt = cnt

# 작아지는 수열 체크
cnt = 1
for i in range(1,n):
    if nums[i] <= nums[i-1]:
        cnt += 1
    else:
        cnt = 1
    if cnt > max_cnt:
        max_cnt = cnt
print(max_cnt)