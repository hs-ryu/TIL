

'''
문제
N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.
아래는 N=5 의 예이다.
M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.
죽은 파리의 개수를 구하라!
예를 들어 M=2 일 경우 위 예제의 정답은 49마리가 된다.
[제약 사항]
1. N 은 5 이상 15 이하이다.
2. M은 2 이상 N 이하이다.
3. 각 영역의 파리 갯수는 30 이하 이다.

[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고,
그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
다음 N 줄에 걸쳐 N x N 배열이 주어진다.


[출력]

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''

#막힘없이 풀었다. 지렸다 현선아
#몇번 테스트 할건지 입력
t = int(input())

#t번 테스트 돌린다.
for i in range(t):

    #n (영역 크기 : nxn), m (파리채 크기 : mxm) 
    n,m = map(int,input().split())
    #숫자 리스트로 그려질 영역
    area = []
    #최대값 비교를 위한 변수
    max_value = 0

    #n번 입력받아 숫자로 이루어진 영역 만든다.
    for _ in range(n):
        area.append(list(map(int,input().split())))

    #행 바꿈을 위한 반복 k = 행
    for k in range(0, n - m + 1):
        # 열 바꿈을 위한 반복 s = 열
        for s in range(0, n - m + 1):
            #파리채에 잡힌 파리의 합을 저장할 변수 value
            value = 0
            #파리채가 한칸씩 움직이며 잡을 수 있는 파리의 수를 value에 저장
            for j in range(k, k+m):
                #area를 슬라이싱 하는것은 리스트를 가져오는 것이므로, sum을 해서 value에 더해줌.
                value += sum(area[j][s:s+m])
            #만약 현재 저장된 value가 max_value보다 크다면.
            #그 값을 max_value에 저장해 줌.
            #즉 마지막에는 max_value에 최대값만 남아 있을것!
            if value > max_value:
                max_value = value
    #출력출력 ez
    print('#{0} {1}'.format(i+1,max_value))

    