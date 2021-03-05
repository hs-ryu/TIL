import sys
sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T + 1):
    D = list(map(int, input().rstrip()))

    panbyul = False
    for i in range(len(D)):
        for j in range(len(D)):
            if i != j:
                for k in range(len(D)):
                    if k != i and k != j:
                        for l in range(len(D)):
                            if l != i and l != j and l != k:
                                for m in range(len(D)):
                                    if m != i and m != j and m != k and m != l:
                                        for n in range(len(D)):
                                            if n != i and n != j and n != k and n != l and n != m:
                                                # print(D[i], D[j], D[k], D[l], D[m], D[n])
                                                if (D[i] + 1 == D[j] and D[j] + 1 == D[k]) and (
                                                        D[l] + 1 == D[m] and D[m] + 1 == D[n]):
                                                    panbyul = True
                                                if (D[i] + 1 == D[j] and D[j] + 1 == D[k]) and (D[l] == D[m] == D[n]):
                                                    panbyul = True
                                                if (D[i] == D[j] == D[k]) and (D[l] + 1 == D[m] and D[m] + 1 == D[n]):
                                                    panbyul = True
                                                if (D[i] == D[j] == D[k]) and (D[l] == D[m] == D[n]):
                                                    panbyul = True
    if panbyul:
        print('#%d %s' % (t, 'Baby Gin'))
    else:
        print('#%d %s' % (t, 'Lose'))








    '''
    for i in range(len(D)):
        for j in range(len(D)):
            if D[i] != D[j]:
                for k in range(len(D)):
                    if D[k] != D[i] and D[k] != D[j]:
                        for l in range(len(D)):
                            if D[l] != D[i] and D[l] != D[j] and D[l] != D[k]:
                                for m in range(len(D)):
                                    if D[m] != D[i] and D[m] != D[j] and D[m] != D[k] and D[m] != D[l]:
                                        for n in range(len(D)):
                                            if D[n] != D[i] and D[n] != D[j] and D[n] != D[k] and D[n] != D[l] and D[m] != D[m]:
                                                print(D[i], D[j], D[k], D[l], D[m], D[n])
                                                '''

