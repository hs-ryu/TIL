'''
문제
1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.
[예제 풀이]
N이 5일 경우,
1 – 2 + 3 – 4 + 5 = 3
N이 6일 경우,
1 – 2 + 3 – 4 + 5 – 6 = -3
[제약사항]
N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)


[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스에는 N이 주어진다.

[출력]
각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 누적된 값을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''







#ez
#테스트 몇번 할건지 입력받음
t = int(input())
#입력받은 수만큼 반복
for i in range(t):
    #숫자를 입력받음
    n = int(input())
    #결과를 반환할 result 변수 선언
    result = 0

    #1~n까지 더할건데
    for j in range(1,n+1):
        #짝수면 -로 해서 더함
        if not j % 2:
            result += -j
        #홀수면 그냥 더함
        else:
            result += j
    #출력
    print('#{0} {1}'.format(i+1, result))