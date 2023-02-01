# 효율성 0점. 배열 중간에 pop하는 과정이 O(N)이라서 그런듯함.
# 스택으로 하면?
def solution(s):
    answer = 1
    a = list(s)
    i = 0
    while i < len(a)-1:
        if len(a) == 0:
            break
        if a[i] == a[i+1]:
            a.pop(i)
            a.pop(i)
            if i > 0:
                i -= 1
        else:
             i += 1
    if len(a) != 0:
        answer = 0
    return answer

# 좋다. 효율성 100점!
def solution(s):
    answer = 1
    stack = []
    i = 0
    while i < len(s):
        if stack:
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])
        i += 1
    if stack:
        answer = 0
    
    return answer