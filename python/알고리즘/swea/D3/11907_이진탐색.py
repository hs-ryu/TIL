import sys
sys.stdin = open('5207_input.txt')



'''
a = [1,3,5,6,7,10,14,16,17,19]
left = 0
right = len(a) - 1

6을 찾는다고 할때

m = (left + right) // 2 = (0+9)//2 = 4
a[4] = 7
7은 6보다 크니까
따라서, right = m-1로 바까줌

다시 m 구해주고
m = (left + right) // 2 = (0+3)//2 = 1
a[1] = 3
3은 6보다 작으니까
left = m+1

다시 m 구해주고
m = (left+right) // 2 = (2+3)//2 = 2
a[2] = 5
5는 6보다 작으니까
left = m+1

다시 m 구해주고
m = (left+right) // 2 = (2+3)//2 = 3
a[3] = 6 찾았다!
'''

# 원하는 결과를 얻었던가, left <= right일 때 까지.

def bin_search(A, x, left, right):
    flag = 0
    while left <= right:
        m = (left + right) // 2
        if A[m] == x:
            return 1
        elif A[m] > x:
            if flag == -1:
                return 0
            right = m-1
            flag = -1
        elif A[m] < x:
            if flag == 1:
                return 0
            left = m+1
            flag = 1
    return 0


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    result = 0
    for i in B:
        result += bin_search(A, i, 0, N-1)
    print('#%d %d' %(t, result))




# A, B => A배열에서 B의 각요소를 이진탐색을 이용해 찾을 때 비교횟수 누적값 출력, 못찾았다면 0이라고 하자
