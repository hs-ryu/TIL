def quick(left, right, pivot):
    if left >= right:
        return
    i = j = left
    while j < right:
        if arr[j] > pivot:
            j += 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
    arr[i], arr[right] = arr[right] , arr[i]
    print(*arr)
    quick(left, i-1, arr[i-1])
    quick(i+1, right, arr[right])

    
N = int(input())
arr = list(map(int, input().split()))
quick(0, N-1, arr[-1])
