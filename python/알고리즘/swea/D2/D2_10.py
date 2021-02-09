'''
N x N 행렬이 주어질 때,

시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.


[제약 사항]

N은 3 이상 7 이하이다.

[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에 N이 주어지고,

다음 N 줄에는 N x N 행렬이 주어진다.

[출력]

출력의 첫 줄은 '#t'로 시작하고,

다음 N줄에 걸쳐서 90도, 180도, 270도 회전한 모양을 출력한다.

입력과는 달리 출력에서는 회전한 모양 사이에만 공백이 존재함에 유의하라.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


'''

#존나 씨발 힘들었다. 
import copy
t = int(input())
for i in range(t):
    n = int(input())
    m = list()
    for j in range(n):
        m.append(list(input().split()))
    result = []
    for _ in range(3):
        
        m1 = copy.deepcopy(m)
        for x in range(len(m)):
            for y in range(len(m)):
                m[y][x] = m1[x][len(m)-1-y]
        #여기까진 ez..
        #왜 시발 한번더 딥카피 써야하지? m이 그대로 result에 추가되도 될거 같은데.
        m2 = copy.deepcopy(m)
        result.extend(m2)
    print(f'#{i+1}')
    #이거 보다 더 좋은 출력 방법 없을까? 조인해서 추가하는 방법....? 일단 안되니까 패스.
    for q in range(len(m)):
        print(''.join(result[q+2*n]), ''.join(result[q+n]), ''.join(result[q]))
