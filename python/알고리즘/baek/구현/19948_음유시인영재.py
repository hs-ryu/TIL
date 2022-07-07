poem = input()
spacebar = int(input())
possible_alpha = list(map(int,input().split()))

alpha = dict()
for i in range(26):
    alpha[chr(65+i)] = possible_alpha[i]

count_alpha = dict()
for i in range(len(poem)):
    k = poem[i].upper()
    if k in count_alpha:
        count_alpha[k] += 1
    else:
        count_alpha[k] = 1



for alpha in count_alpha.keys():
    if alpha == " ":
        if count_alpha[alpha] > spacebar:
            print(-1)
            break
    else:
        if count_alpha[alpha] > possible_alpha[alpha]:
            print(-1)
            break
else:
    poem = poem.split()
    result = ""
    for i in range(len(poem)):
        result += poem[i][0]
    print(result)
