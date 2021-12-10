# # a b c d e f g h i j k l m n o p q r s t u v w x y z
# # w g h u v i j x p q r s t a c d e b f k l m n o y z

# t = int(input())

# # 97 ~ 122

# ciphertoorigin = {'w': 'a', 'g': 'b', 'h': 'c', 'u': 'd', 'v': 'e', 'i': 'f', 'j': 'g', 'x': 'h',
#                   'p': 'i', 'q': 'j', 'r': 'k', 's': 'l', 't': 'm', 'a': 'n',
#                   'c': 'o', 'd': 'p', 'e': 'q', 'b': 'r', 'f': 's', 'k': 't',
#                   'l': 'u', 'm': 'v', 'n': 'w', 'o': 'x', 'y': 'y', 'z': 'z'}
# dic = dict()

# for _ in range(t):
#     s = input()
#     for i in range(len(s)):
#         if s[i] in dic:
#             dic[s[i]] += 1
#         else:
#             dic[s[i]] = 1
#     sorted_list = sorted(dic.items(), key=lambda x: -x[1])

#     if len(sorted_list) > 1:
#         if sorted_list[0][1] == sorted_list[1][1]:
#             result = '?'
#         else:
#             result = ciphertoorigin[sorted_list[0][0]]
#     else:
#         result = ciphertoorigin[sorted_list[0][0]]

#     print(result)


t = int(input())

for _ in range(t):
    s = input().replace(' ','')
    dic = dict()
    for i in range(len(s)):

        if s[i] in dic:
            dic[s[i]] += 1
        else:
            dic[s[i]] = 1
    sorted_list = sorted(dic.items(), key=lambda x: -x[1])

    if len(sorted_list) > 1:
        if sorted_list[0][1] == sorted_list[1][1]:
            result = '?'
        else:
            result = sorted_list[0][0]
    else:
        result = sorted_list[0][0]
    print(result)
