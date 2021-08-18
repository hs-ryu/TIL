# def merge(arr):
#     if len(arr) == 1:
#         return arr
#     middle = len(arr)//2
#     left_arr = merge(arr[:middle])
#     right_arr = merge(arr[middle:])
#     sorted_arr = []
#     i = j = 0
#     while i < len(left_arr) and j < len(right_arr):
#         if left_arr[i] < right_arr[j]:
#             sorted_arr.append(left_arr[i])
#             i += 1
#         else:
#             sorted_arr.append(right_arr[i])
#             j += 1
#     sorted_arr.extend(left_arr[i:])
#     sorted_arr.extend(right_arr[j:])
#     return sorted_arr        


def merge(arr, left, right, sorted_arr):
    if left >= right:
        return
    # 분할
    middle = (left + right)//2

    # 정복
    merge(arr, left, middle, sorted_arr)
    merge(arr, middle+1, right, sorted_arr)

    # 병합
    i = left
    j = middle + 1
    for k in range(left, right+1):
        if j > right:
            sorted_arr[k] = arr[i]
            i += 1
        elif i > middle:
            sorted_arr[k] = arr[j]
            j += 1
        elif arr[i] <= arr[j]:
            sorted_arr[k] = arr[i]
            i += 1
        else:
            sorted_arr[k] = arr[j]
            j += 1
        
        
    
    # 복사
    for i in range(left, right+1):
        arr[i] = sorted_arr[i]
    
    print(*arr)

n = int(input())
arr = list(map(int,input().split()))
sorted_arr = [0] * n
merge(arr, 0, n-1, sorted_arr)

