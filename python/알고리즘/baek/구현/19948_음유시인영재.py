
# 100% 에서 틀림...
poem = input()
spacebar = int(input())
possible_alpha = list(map(int,input().split()))

alpha = dict()
for i in range(26):
    alpha[chr(65+i)] = possible_alpha[i]
alpha[" "] = spacebar
count_alpha = dict()
count_alpha[poem[0].upper()] = 1
for i in range(1,len(poem)):
    if poem[i] == poem[i-1]:
        continue
    if poem[i].upper() in count_alpha:
        count_alpha[poem[i].upper()] += 1
    else:
        count_alpha[poem[i].upper()] = 1
for k in count_alpha.keys():
    v = count_alpha[k]
    if v > alpha[k]:
        print(-1)
        break
else:
    poem = poem.split()
    result = ""
    for i in range(len(poem)):
        result += poem[i][0].upper()
    print(result)