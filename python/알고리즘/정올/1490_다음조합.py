def nCr(n,arr,r):
    if n == N:
        if len(arr) == r:
            global flag
            if flag == 1:
                global ans_flag
                print(*arr)
                flag = 0
                ans_flag = 1
            x = ''
            for i in range(len(arr)):
                x += str(arr[i])
                if x == find_str:
                    flag = 1
        return
    arr.append(nums[n])
    nCr(n+1,arr,r)
    arr.pop()
    nCr(n+1,arr,r)

N, k = map(int, input().split())
nums = [i for i in range(1,N+1)]
find = input().split()
find_str = ''.join(find)
flag = 0
ans_flag = 0
nCr(0,[],k)
if ans_flag == 0:
    print('NONE')