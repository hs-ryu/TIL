import sys
sys.stdin = open('s_input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())

    # 아 5000개를...............만들어서 해야하구나......
    bus = [0] * 5001
    A = []
    B = []
    for i in range(N):
        x = list(map(int, input().split()))
        A.append(x[0])
        B.append(x[1])
    for i in range(N):
        for j in range(A[i], B[i]+1):
            bus[j] += 1
    P = int(input())
    result = []
    for i in range(P):
        C = int(input())
        result.append(bus[C])
    res = ' '.join(list(map(str, result)))
    print('#%d %s' %(t, res))


'''
T = int(input())
for t in range(1, T+1):
    N = int(input())
    
    bus_stop = [0] * 5001
    
    for i in range(N):
        A, B = map(int,input().split())
        
        # 해당 정류장에 지나는 버스의 대수 누적
        for j in range(A, B+1):
            bus_stop[j] += 1
            
    P = int(input()) #우리가 확인하고 싶은 버스 정류장의 수
    
    print('#{}'.format(t), end=' ')
    for i in range(P):
        C = int(input()) #우리가 확인하고 싶은 정류장의 번호
        print(bus_stop[C], end=' ')
    print()
            

'''