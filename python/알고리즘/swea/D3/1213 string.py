import sys
sys.stdin = open('test_input.txt', encoding='utf-8')


for t in range(1, 11):
    T = int(input())
    find_str = input()
    sentence = input()
    cnt = 0
    for i in range(len(sentence) - len(find_str) + 1):
        if sentence[i:i+len(find_str)] == find_str:
            cnt += 1
    print('#%d %d' %(t,cnt))

    # 보이어-무어 방식..... 다시 짜보기.....

    '''
    #못찾으면 비교해서 인덱스 만큼 스킵할 수 있게 skip 배열 만들어줌
    skip = []
    for i in range(len(find_str)-1, -1, -1):
        skip.append(find_str[i])
    print(len(sentence))
    
    i = 0
    cnt = 0
    while i < len(sentence)-len(skip):
        x = 0
        for j in range(len(skip)):
            if skip[j] != sentence[i + (len(skip) - j - 1)]:
                if sentence[i + (len(skip) - j)] in skip:
                    i += skip.index(sentence[i + (len(skip) - j)])
                else:
                    i += len(skip)
                break
        else:
            cnt += 1
            i += 1
        print(i)
    print('x')

'''






