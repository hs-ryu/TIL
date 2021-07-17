def search(index, num, s):
    if num == s:
        if len(k) == 0:
            numset.add(num)
        else:
            for j in k:
                numset.add(j)
        return
    if index in k:
        return
    k.append(index)
    search(num, nums[num], s)

n = int(input())
indexs = [i for i in range(n+1)]
nums = [0]
flag=0
numset = set()

for i in range(n):
    nums.append(int(input()))
for i in range(1,n+1):
    k = []
    search(indexs[i], nums[i], indexs[i])
result = sorted(list(numset))
print(len(result))
for i in result:
    print(i)