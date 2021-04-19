import sys
sys.stdin = open('5204_input.txt')

def merge(arr):
    global cnt
    # 길이가 1이면 더이상 반으로 못나누니까 종료
    if len(arr) == 1:
        return arr
    middle = len(arr) // 2
    left_arr = merge(arr[:middle])
    right_arr = merge(arr[middle:])
    if left_arr[-1] > right_arr[-1]:
        cnt += 1
    sorted_arr = []
    i = j = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            sorted_arr.append(left_arr[i])
            i += 1
        else:
            sorted_arr.append(right_arr[j])
            j += 1
    # 남은 아이템들 넣기
    sorted_arr.extend(left_arr[i:])
    sorted_arr.extend(right_arr[j:])
    return sorted_arr

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    result = merge(arr)
    # print(result)
    print('#%d %d %d' %(t, result[N//2] , cnt))