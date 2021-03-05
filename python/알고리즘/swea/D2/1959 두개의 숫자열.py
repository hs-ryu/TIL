import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    n_list = list(map(int, input().split()))
    m_list = list(map(int, input().split()))
    max_num = 0
    if n > m:
        for j in range(n - m):
            x = 0
            for k in range(m):
                x += n_list[k+j] * m_list[k]
            if x > max_num:
                max_num = x
    elif n < m:
        for j in range(m - n + 1):
            x = 0
            for k in range(n):
                x += n_list[k] * m_list[k+j]
            if x > max_num:
                max_num = x
    else:
        for j in range(n):
            x = 0
            for k in range(n):
                x += n_list[k] * m_list[k]
            if x > max_num:
                max_num = x
    print('#%d %d' % (t, max_num))



'''
def check(long,short):
    max_value = -987654321
    for i in range(len(long)-len(short)-1):
        result = 0
        for j in range(len(short)):
            result += long[i+j]*short[j]
        
        if max_value < result:
            max_value = result
    return max_value

T = int(input())

for tc in range(1,T+1):
    # N, M  리스트의 길이를 의미한다.
    N, M = map(int,input().split())
    
    A = list(map(input().split()))
    B = list(map(input().split()))
    
    if N > M:
        ans = check(A,B)
    else:
        ans = check(B,A)
       
    

'''