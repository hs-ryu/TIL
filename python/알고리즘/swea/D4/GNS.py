# 정렬문제...
# 1. 카운팅 정렬 사용해보기.
# 2. 수업에서 배운 특별한 정렬 사용해보기.

'''
숫자 체계가 우리와 다른 어느 행성이 있다. 아래는 이 행성에서 사용하는 0 ~ 9의 값을 순서대로 나타낸 것이다.

"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"

0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부터 차례로 정렬하여 출력하는 프로그램을 작성하라.

예를 들어 입력 문자열이 "TWO NIN TWO TWO FIV FOR" 일 경우 정렬한 문자열은 "TWO TWO TWO FOR FIV NIN" 이 된다.

[입력]

입력 파일의 첫 번째 줄에는 테스트 케이스의 개수가 주어진다.

그 다음 줄에 #기호와 함께 테스트 케이스의 번호가 주어지고 공백문자 후 테스트 케이스의 길이가 주어진다.

그 다음 줄부터 바로 테스트 케이스가 주어진다. 단어와 단어 사이는 하나의 공백으로 구분하며, 문자열의 길이 N은 100≤N≤10000이다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 정렬된 문자열을 출력한다.
'''


import sys
sys.stdin = open('GNS_test_input.txt')

# def counting_sort():

num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for t in range(1,T+1):
    length = int(input().split()[1])
    arr = list(input().split())
    cnt = [0 for i in range(len(num))]
    result = [0 for i in range(len(arr))]
    # 카운팅 정렬 사용. 1차 제출
    for i in range(len(arr)):
        cnt[num.index(arr[i])] += 1
    for i in range(1, len(cnt)):
        cnt[i] += cnt[i-1]
    for i in range(len(result)-1, -1, -1):
        result[cnt[num.index(arr[i])]-1] = num[num.index(arr[i])]
        cnt[num.index(arr[i])] -= 1
    print('#%d' %t)
    print(*result)

# 수업시간에 배운 정렬 방식 사용해보기. 할 수 있을듯. -> 주말에 꼭하자
# 함수로도 작성해보기.