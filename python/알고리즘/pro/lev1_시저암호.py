def solution(s, n):
    answer = ''
    for i in range(len(s)):
        # print(ord(s[i]))
        if (65 <= ord(s[i]) <= 90):
            if ord(s[i]) + n <= 90:
                answer += chr(ord(s[i]) + n)
            else:
                answer += chr(ord(s[i]) + n - 26)
        elif (97 <= ord(s[i]) <= 122):
            if ord(s[i]) + n <= 122:
                answer += chr(ord(s[i]) + n)
            else:
                answer += chr(ord(s[i]) + n - 26)
        else:
            answer += s[i]
                
    return answer