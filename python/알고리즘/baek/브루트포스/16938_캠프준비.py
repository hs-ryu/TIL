# 둘다 시간초과...


def search(level, arr):
    # print(arr,level)
    if len(arr) >= 2:
        
        if set(arr) not in result_list:
            new_arr = [0] * len(arr)
            for i in range(len(arr)):
                new_arr[i] = a[arr[i]]
            # print(arr)
            # print(new_arr, "??")
            hab = sum(new_arr)
            maxv = max(new_arr)
            minv = min(new_arr)
            if hab >= l and hab <= r and maxv - minv >= x:
                result_list.append(set(arr))
    if level == n:
        return
    

    arr.append(b[level])
    search(level+1,arr)
    arr.pop(-1)
    search(level+1,arr)



n,l,r,x = map(int,input().split())
a = list(map(int,input().split()))
b = [i for i in range(n)]
# print(b)
result_list = []
visited = [0] * n


search(0,[])

# print(result_list)
print(len(result_list))