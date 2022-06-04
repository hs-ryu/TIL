
# 마지막 테캐 통과 못함.
def solution(s):
    answer = 0
    s = list(s)
    i = 0
    while i < len(s):
        k = s.pop(0)
        s.append(k)
        check = 0
        s_cnt = 0
        m_cnt = 0
        l_cnt = 0
        for j in range(len(s)):
            if s[j] == "(":
                s_cnt += 1
            elif s[j] == ")":
                s_cnt -= 1
            elif s[j] == "[":
                m_cnt += 1
            elif s[j] == "]":
                m_cnt -= 1
            elif s[j] == "{":
                l_cnt += 1
            else:
                l_cnt -= 1
            if s_cnt < 0 or m_cnt < 0 or l_cnt < 0:
                check = 1
                break
        if s_cnt != 0 or m_cnt != 0 or l_cnt != 0:
            i += 1
            continue
        if check == 0:
            answer += 1
        i += 1
        
    return answer

# 굳!
def solution(s):
    answer = 0
    open_list = []
    open_set = {'{','[','('}
    s = list(s)
    i = 0
    while i < len(s):
        k = s.pop(0)
        s.append(k)
        
        for j in range(len(s)):
            if s[j] in open_set:
                open_list.append(s[j])
            else:
                if len(open_list) == 0:
                    break
                x = open_list.pop(-1)
                if s[j] == ")":
                    if x != "(":
                        break
                elif s[j] == "}":
                    if x != "{":
                        break
                else:
                    if x != "[":
                        break
        else:
            if len(open_list) == 0:
                answer += 1
        i += 1
    return answer