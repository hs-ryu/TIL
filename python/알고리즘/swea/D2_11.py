'''
문제
N 개의 숫자로 구성된 숫자열 Ai (i=1~N) 와 M 개의 숫자로 구성된 숫자열 Bj (j=1~M) 가 있다.
아래는 N =3 인 Ai 와 M = 5 인 Bj 의 예이다.
Ai 나 Bj 를 자유롭게 움직여서 숫자들이 서로 마주보는 위치를 변경할 수 있다.
단, 더 긴 쪽의 양끝을 벗어나서는 안 된다.
서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하라.
위 예제의 정답은 아래와 같이 30 이 된다.
 
[제약 사항]

N 과 M은 3 이상 20 이하이다.


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,

두 번째 줄에는 Ai,

세 번째 줄에는 Bj 가 주어진다.

[출력]

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''


#몇 번 테스트 돌릴 것인지 입력 받음.
t = int(input())
#입력 받은 수만큼 테스트
for i in range(t):
    #각 리스트의 길이를 정의할 n,m
    n,m = map(int,input().split())
    #숫자 배열을 저장할 리스트 n,m_mlist
    n_list = list(map(int,input().split()))
    m_list = list(map(int,input().split()))
    #총 3가지 경우. 둘 중 하나의 길이가 길던가, 아니면 똑같던가
    #n의 m 보다 클 경우
    if n >m:
        max_num = 0
        #이중 for문을 써서, 각 맞라인 곱을 더해줌. 계산 끝나면 길이가 작은게 한칸씩 옆으로 움직이게 함.
        for j in range(n - m):
            x = 0
            for k in range(m):
                x += n_list[k+j] * m_list[k]
            #만약 더해준 값이 max_num보다 크다면, max_num에 해당 값을 저장.
            if x > max_num:
                max_num = x
    #m이 n보다 클 경우
    elif m > n:
        max_num = 0
        for j in range(m - n + 1):
            x = 0
            for k in range(n):
                x += n_list[k] * m_list[k+j]
            if x > max_num:
                max_num = x
    #길이가 같은 경우
    else:
        max_num = 0
        for j in range(n):
            x = 0
            for k in range(n):
                x += n_list[k] * m_list[k]
            if x > max_num:
                max_num = x
    #출력
    print(f'#{i+1} {max_num}')