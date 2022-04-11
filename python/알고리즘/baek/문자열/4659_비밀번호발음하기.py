m = ['a','e','i','o','u']


while True:
    word = input()
    f_flag = 0
    check = 0
    if word == "end":
        break
    
    # 1번 조건 체크
    for i in range(len(word)):
        if word[i] in m:
            f_flag = 1
            break
    
    m_cnt = 0
    j_cnt = 0
    for i in range(len(word)):
        if word[i] in m:
            m_cnt += 1
            j_cnt = 0
        else:
            m_cnt = 0
            j_cnt += 1
        if m_cnt == 2 or j_cnt == 2:
            if word[i-1] == word[i]:
                if word[i-1:i+1] != "ee" and word[i-1:i+1] != "oo":
                    check = 1
                    break
        if m_cnt == 3 or j_cnt == 3:
            check = 1
            break
     
    if not check and f_flag:
        print("<{0}> is acceptable.".format(word))
    else:
        print("<{0}> is not acceptable.".format(word))