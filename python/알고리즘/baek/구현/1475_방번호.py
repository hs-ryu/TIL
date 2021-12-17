n = input()
nums = {i : 0 for i in range(10)}


sixornine = 0
for i in range(len(n)):
    num = int(n[i])
    if (num == 6 or num == 9):
        sixornine += 1
    else:
        nums[num] += 1
if sixornine % 2:
    nums[6] = sixornine//2 + 1
else:
    nums[6] = sixornine//2
print(max(nums.values()))
