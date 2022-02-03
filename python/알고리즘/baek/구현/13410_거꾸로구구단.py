n,k = map(int,input().split())
nums = []
for i in range(1,k+1):
    num = str(n * i)
    nums.append(list(num))
# print(nums)
for i in range(k):
    nums[i].reverse()
    nums[i] = int("".join(nums[i]))
print(max(nums))


# 더 짧게

n,k = map(int,input().split())
maxn = 0
for i in range(1,k+1):
    num = list(str(n * i))
    num.reverse()
    num = int("".join(num))
    if num > maxn:
        maxn = num
print(maxn)