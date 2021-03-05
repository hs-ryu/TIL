import sys
sys.stdin = open('sample_input1.txt')

# 정렬하고 하나씩 빼오는 방법 있음. 근데 굳이 두번 일을? -> 이거 먼저 해보자.
# 이중 반복문 안에, 범위 안에서 가장 큰 값의 인덱스를 불러와서 인덱스를 바꿔주는 방식으로도 가능할 것 같음. if문을 통해 분기 가능!
def salt(x):
    for i in range(len(x)-1,0,-1):
        for j in range(i):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    return x


T = int(input())
for t in range(1, T+1):
    N = int(input())
    A = [i for i in list(map(int,input().split()))]
    result = [0] * 10
    sort_A = salt(A)
    print(sort_A)
    for i in range(len(result)):
        if i % 2 == 0:
            result[i] = sort_A[-1-int(i/2)]
        else:
            result[i] = sort_A[int(i/2)]
    result_str = ' '.join(map(str, result))
    print('#%d %s' %(t, result_str))
#             오름차순 정렬
#             result[i] = minV


