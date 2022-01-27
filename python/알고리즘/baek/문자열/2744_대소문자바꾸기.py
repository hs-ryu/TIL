# s = input()
# answer = []
# for i in range(len(s)):
#     if s[i].isupper():
#         answer.append(s[i].lower())
#     else:
#         answer.append(s[i].upper())
# print("".join(answer))


# 혹은 딕셔너리 선언으로 변경 가능. 메모리 사용량과 시간은 위와 동일
s = input()
answer = []

alpha = {chr(i):i for i in range(97,123)}
ALPHA = {chr(i):i for i in range(65,91)}
for a in s:
    if a in alpha:
        answer.append(chr(alpha[a] - 32))
    else:
        answer.append(chr(ALPHA[a] + 32))
print("".join(answer))