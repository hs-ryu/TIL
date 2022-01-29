
# 시간초과
# from itertools import permutations

# # # product : 중복 순열 -> 모든 조합. 중복 허용.
# # # permutation : 순열
# # # combination : 조합 
# n = int(input())

# for _ in range(n):
#     string = input()
#     arr = permutations(string, len(string))
#     answer = list(set(arr))
#     # print(answer)
#     result = []
#     for i in range(len(answer)):
#         result.append(''.join(answer[i]))
#     result.sort()
#     for index,st in enumerate(result):
#         if st == string:
#             break
#     # print(index)
#     dab = st if index == len(result)-1 else result[index+1]
#     print(dab)
    

    


# B E E R
# B 

def search(word):
    temp = word[-1]
    result = []

    for i in range(len(word)-2,-1,-1):
        result.append(temp)
        # 현재의 문자가 더 사전순으로 느리다면
        if ord(word[i]) < ord(temp):
            # print(temp)
            result.append(word[i])
            result.sort()
            print(result)

            for j in range(len(result)):
                # word[i] = I
                if ord(result[j]) > ord(word[i]):
                    next = result.pop(j)
                    break
            # DR + 
            return word[:i] + next + "".join(result)
        # 현재의 문제가 사전순으로 더 빠르다면
        else:
            temp = word[i]
    # 마지막이면 word 그대로 출력
    return word

n = int(input())
for _ in range(n):
    word = input()
    result = search(word)
    print(result)


