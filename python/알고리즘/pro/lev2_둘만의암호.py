def solution(s, skip, index):
    answer = ''
    x = list(skip)
    y = set()
    for i in x:
        y.add(ord(i))

    for i in range(len(s)):
        st = s[i]
        n = ord(st)
        k = 0
        while k < index:
            k += 1
            n += 1
            if n in y:
                k -= 1
            if n == 123:
                n = 97
                if n in y:
                    k -= 1
        r = chr(n)
        answer += r
    
    return answer