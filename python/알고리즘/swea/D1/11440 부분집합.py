import sys
sys.stdin = open('ex02_input.txt')

def suum(x):
    s = 0
    for i in x:
        s += i
    return s

T = int(input())
for t in range(1, T+1):
    N = list(map(int, input().split()))
    x = []
    for i in range(1<<len(N)):
        y = []
        for j in range(len(N)+1):
            if i & 1<<j:
                y.append(N[j])
        x.append(y)
    for i in x[1:]:
        result = suum(i)
        if result == 0:
            print('#%d %d' %(t,1))
            break
    else:
        print('#%d %d' % (t, 0))




'''
T = int(input())
for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    n = 10 
    for i in range(1, 1 << n):   # 이 부분
        subset_sum = 0
        for j in range(n + 1):
            if i & (1 << j):
                subset_sum += numbers[j]
        if subset_sum == 0:
            print('#%s 1' % t)
            break
    else:
        print('#%s 0' % t)
'''

# def bubun(x):
#     n = len(x)
#     for i in range(1, 1<<n):
#         subset_sum = 0
#         for j in range(n + 1):
#             if i & (1 << j):
#                 subset_sum += numbers[j]
#             if subset_sum == 0:
#                 return 1
#     return 0




