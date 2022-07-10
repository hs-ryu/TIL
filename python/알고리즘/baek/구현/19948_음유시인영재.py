
# 100% 에서 틀림...
poem = input()
spacebar = int(input())
possible_alpha = list(map(int,input().split()))

# 입력받은 알파벳 제한을 넣어줄 딕셔너리
alpha = dict()
for i in range(26):
    alpha[chr(65+i)] = possible_alpha[i]
# 스페이스바도 넣어주고
alpha[" "] = spacebar

# 문자열 돌면서 카운트 측정
count_alpha = dict()
count_alpha[poem[0].upper()] = 1
for i in range(1,len(poem)):
    if poem[i] == poem[i-1]:
        continue
    if poem[i].upper() in count_alpha:
        count_alpha[poem[i].upper()] += 1
    else:
        count_alpha[poem[i].upper()] = 1

# 측정한 개수와, 제한 사항 비교
for k in count_alpha.keys():
    v = count_alpha[k]
    if v > alpha[k]:
        print(-1)
        break
# 브레이크 안걸리면, 문제 없는거임.
else:
    poem = poem.split()
    result = ""
    for i in range(len(poem)):
        result += poem[i][0].upper()
    print(result)