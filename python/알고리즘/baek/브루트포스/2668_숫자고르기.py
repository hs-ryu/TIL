def search(index, num):
    # 고리 만들어지면, 위, 아래가 다 들어간거임.
    if num == first:
        # 5,5 처럼 num과 index값이 동일하다면, 바로 넣어주면됨.
        if len(arr) == 0:
            numset.add(num)
        # 그게 아니면, 고리만들면서 arr에 넣어준 값들을 set에 넣어준다.
        else:
            for j in arr:
                numset.add(j)
        return
    # 얘 처리 해줘야하네..
    if index in arr:
        return
    arr.append(index)
    # 다음 재귀에서는 num이 index값이 되어야함. num은 nums의 해당 인덱스 값으로.
    search(num, nums[num])

n = int(input())
indexs = [i for i in range(n+1)]
nums = [0]
numset = set()

for i in range(n):
    nums.append(int(input()))

for i in range(1,n+1):
    arr = []
    first = indexs[i]
    search(indexs[i], nums[i])
# 굳!!

result = sorted(list(numset))
print(len(result))
for i in result:
    print(i)