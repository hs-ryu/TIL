'''
문제
크기가 N인 파스칼의 삼각형을 만들어야 한다.
파스칼의 삼각형이란 아래와 같은 규칙을 따른다.
1. 첫 번째 줄은 항상 숫자 1이다.
2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.
N이 4일 경우, N을 입력 받아 크기 N인 파스칼의 삼각형을 출력하는 프로그램을 작성하시오.
[제약 사항]
파스칼의 삼각형의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스에는 N이 주어진다.
[출력]
각 줄은 '#t'로 시작하고, 다음 줄부터 파스칼의 삼각형을 출력한다.
삼각형 각 줄의 처음 숫자가 나오기 전까지의 빈 칸은 생략하고 숫자들 사이에는 한 칸의 빈칸을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''

#테스트 케이스 몇번 실행할건지 입력
a = int(input())

#입력한 수만큼 반복
for i in range(a):

    #몇 줄을 출력할건지 입력
    b = int(input())
    
    #빈 리스트 answer. 여기에 값 채우고 바꿔서 출력할거임
    answer = []

    #일단, 모든 줄의 요소을 다 1로 채워서 answer에 넣어줌.
    for j in range(1,b+1):
        answer.append([1] * j)

    #2번 줄부터 마지막 줄까지만 변경하면 되니까 2~b까지 설정.
    for k in range(2,b):
        
        #이때, 해당 줄의 1번 요소부터 마지막-1번 요소까지만 해주면 되니까 해당 범위에서 값 변경 실행.
        for m in range(1,k):

            #k=3, m=2 번 요소를 바꾼다고 가정하면 2번줄의 1번 값(2)에 2번줄의 2번값(1)을 더한 3으로 바까줌
            answer[k][m] = answer[k-1][m-1] + answer[k-1][m]
	
    #몇번째 실행인지 출력
    print('#{0}'.format(i+1))

    #정리된 answer의 모든 값을 출력
    for n in answer:
        print(*n)