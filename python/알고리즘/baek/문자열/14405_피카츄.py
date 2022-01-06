# s = input()

# head = {'p','k','c'}
# check = {'pi', 'ka'}

# i = 0
# cnt = 0
# result = 'NO'
# while i < len(s):
#     print(i)
#     if s[i] in head:
#         # 문자가 c인 경우
#         if s[i] == 'c':
#             # chu다? 그럼 카운트 1 증가 시키고 i를 3 증가시켜줌
#             if s[i:i+3] == 'chu':
#                 cnt += 1
#                 i += 3
#             else:
#                 cnt = 0
#                 i += 1
#         else:
#             if s[i:i+2] in check:
#                 cnt += 1
#                 i += 2
#             else:
#                 cnt = 0
#                 i += 1
#         if cnt == 3:
#             result = 'YES'
#             break
#     else:
#         cnt = 0
#         i += 1
# else:
#     result = 'NO'
# print(result)


s = input()
s = s.replace('pi','1').replace('ka','2').replace('chu','3')

check = {'1','2','3'}

i = 0
while i < len(s):
    if s[i] not in check:
        result = 'NO'
        break
    i += 1
else:
    result = 'YES'
print(result)