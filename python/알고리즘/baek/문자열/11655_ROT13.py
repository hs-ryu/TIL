S = input()

result = ""

for s in S:
    # 대문자
    if 65 <= ord(s) < 91:
        if (ord(s) + 13) > 90:
            result += chr(ord(s) - 13)
        else:
            result += chr(ord(s) + 13)
    elif 97 <= ord(s) < 123:
        if (ord(s) + 13) > 122:
            result += chr(ord(s) - 13)
        else:
            result += chr(ord(s) + 13)
    else:
        result += s

print(result)