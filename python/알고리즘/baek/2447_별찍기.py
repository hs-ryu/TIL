'''
문제
재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.

크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.

***
* *
***
N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다. 예를 들어 크기 27의 패턴은 예제 출력 1과 같다.

입력
첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다. 즉 어떤 정수 k에 대해 N=3k이며, 이때 1 ≤ k < 8이다.

출력
첫째 줄부터 N번째 줄까지 별을 출력한다.
'''
# N > 3인 경우, N의 패턴은 공백으로 채워진 가운데의 (N/3) * (N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태.
'''
N = 27일때
1~3까지 : 3
3~7까지 : 5
7~9까지 : 3
9 ~ 19까지 : 11
19~21까지 : 3
21~25까지 : 5
25~27까지 : 3
'''

from pprint import pprint

def byul(N):
    if N == 3:
        arr[0][:3] = ['*'] * 3
        arr[1][:3] = ['*', ' ', '*']
        arr[2][:3] = ['*'] * 3
    else:
        #만약 N = 9라면?
        #아으앙으ㅡㄴ으음낭ㅁ나엄린ㅁ올ㄴㅇ미로닝뢴어린얼니아리나회널넞더거주피쿠피ㅜㄴ미ㅣㅇ러ㅣ넝리ㅓㄴㅁ런ㅁ;ㄹ
        byul(N//3)
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                for k in range(N//3):
                    # 다시 한번 생각해보기.
                    arr[N//3 * i + k][N//3 * j: N//3 *(j+1)] = arr[k][:N//3]

N = int(input())
arr = [[' ' for i in range(N)] for i in range(N)]
byul(N)
pprint(arr)