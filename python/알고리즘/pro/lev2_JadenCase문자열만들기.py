def solution(s):
    answer = ''
    s = s.split(" ")
    for i in range(len(s)):
        temp = list(s[i])
        for j in range(len(temp)):
            if j == 0:
                if temp[0].isalpha():
                    temp[0] = temp[0].upper()
            else:
                temp[j] = temp[j].lower()
        new_temp = "".join(temp)
        s[i] = new_temp
    answer = " ".join(s)

    return answer