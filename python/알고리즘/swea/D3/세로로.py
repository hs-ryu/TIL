'''
아직 글을 모르는 의석이가 벽에 걸린 칠판에 자석이 붙어있는 글자들을 붙이는 장난감을 가지고 놀고 있다.

이 장난감에 있는 글자들은 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’이다. 의석이는 칠판에 글자들을 수평으로 일렬로 붙여서 단어를 만든다.

다시 그 아래쪽에 글자들을 붙여서 또 다른 단어를 만든다. 이런 식으로 다섯 개의 단어를 만든다. 아래에 의석이가 칠판에 붙여 만든 단어들의 예가 있다.


A A B C D D

a f z z

0 9 1 2 1

a 8 E W g 6

P 5 h 3 k x



만들어진 다섯 개의 단어들의 글자 개수는 서로 다를 수 있다.


심심해진 의석이는 칠판에 만들어진 다섯 개의 단어를 세로로 읽으려 한다.

세로로 읽을 때, 각 단어의 첫 번째 글자들을 위에서 아래로 세로로 읽는다. 다음에 두 번째 글자들을 세로로 읽는다.

이런 식으로 왼쪽에서 오른쪽으로 한 자리씩 이동 하면서 동일한 자리의 글자들을 세로로 읽어 나간다.

위의 그림 1의 다섯 번째 자리를 보면 두 번째 줄의 다섯 번째 자리의 글자는 없다. 이런 경우처럼 세로로 읽을 때 해당 자리의 글자가 없으면, 읽지 않고 그 다음 글자를 계속 읽는다.

그림 1의 다섯 번째 자리를 세로로 읽으면 D1gk로 읽는다.

위에서 의석이가 세로로 읽은 순서대로 글자들을 공백 없이 출력하면 다음과 같다:



Aa0aPAf985Bz1EhCz2W3D1gkD6x



칠판에 붙여진 단어들이 주어질 때, 의석이가 세로로 읽은 순서대로 글자들을 출력하는 프로그램을 작성하라.



[입력]


첫 번째 줄에 테스트 케이스의 수 T가 주어진다.


각 테스트 케이스는 총 다섯 줄로 이루어져 있다.

각 줄에는 길이가 1이상 15이하인 문자열이 주어진다. 각 문자열은 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’만으로 이루어져 있다.


[출력]


각 테스트 케이스마다 #T를 출력하고 한 칸을 띄운 후, 의석이가 세로로 읽은 순서대로 글자들을 출력한다.


'''

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for t in range(1,T+1):
    N = 5
    x = [list(input()) for _ in range(N)]
    max_len = 0
    for i in x:
        if len(i) > max_len:
            max_len = len(i)
    for i in x:
        while len(i) < max_len:
            i.append('')
    result = ''
    for i in range(len(x[0])):
        for j in range(len(x)):
            if x[j][i]:
                result += x[j][i]
    print('#%d %s' %(t,result))

    # zip 쓰면 이렇게 할 수 있다.
    # sero = list(zip(*x))
    # print(sero)
    # result = ''
    # for i in sero:
    #     result += ''.join(i)


    ''' 미친 아이디어.......
    for t in range(1, 2):
    result = [''] * 15  #최대 문자열의 길이가 15로 정해져 있기 때문에 효율적일듯.
    #print(result)
    for _ in range(5):
        word = input()
        for i in range(len(word)):
            result[i] += word[i]
        #print(_, result)
    print('#%s %s' % (t, ''.join(result)))
    '''