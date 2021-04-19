import sys
sys.stdin = open('5205_input.txt')

def quick(left, right, pivot):
    if left >= right:
        return
    # 키 뽀인트. i랑 j값 똑같이 시작하기.
    i = j = left
    while j < right:
        if arr[j] > pivot:
            j += 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
    arr[i], arr[right] = arr[right] , arr[i]
    quick(left, i-1, arr[i-1])
    quick(i+1, right, arr[right])

    
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick(0, N-1, arr[-1])
    print('#%d %d' %(t, arr[N//2]))