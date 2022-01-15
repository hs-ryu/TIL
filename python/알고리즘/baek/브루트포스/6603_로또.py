
def search(arr, s, level):
    if level == 6:
        # 입력 자체가 정렬돼서 들어오니까 굳이 출력할때 정렬 안해줘도됨 ㅎㅎ
        print(*arr)
        return
    for i in range(s,k):
        arr.append(nums[i])
        search(arr,i+1,level+1)
        arr.pop(-1)

nums = list(map(int,input().split()))
k = nums[0]
nums = nums[1:]
while True:    
    search([],0,0)
    nums = list(map(int,input().split()))
    k = nums[0]
    # 입력에 0이 들어오면 break 해준다.
    if k == 0:
        break
    nums = nums[1:]
    print()