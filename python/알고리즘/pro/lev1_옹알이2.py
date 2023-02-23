# 단순 구현문제. 조건처리 잘 하는게 중요!
def solution(babbling):
    answer = 0
    
    word_set = {"aya", "ye", "woo", "ma"}
    
    for word in babbling:
        i = 0
        good = True
        past_word = ""
        while i < len(word):
            if i + 3 <= len(word):
                if word[i:i+3] in word_set:
                    if past_word == word[i:i+3]:
                        good = False
                        break
                    past_word = word[i:i+3]
                    i += 3
                elif word[i:i+2] in word_set:
                    if past_word == word[i:i+2]:
                        good = False
                        break
                    past_word = word[i:i+2]
                    i += 2
                else:
                    good = False
                    break
            elif i + 2 <= len(word):
                if word[i:i+2] in word_set:
                    if past_word == word[i:i+2]:
                        good = False
                        break
                    past_word = word[i:i+2]
                    i += 2
                else:
                    good = False
                    break
            else:
                good = False
                break
        if good:
            answer += 1
    
    return answer
# 혹은, 아래처럼 replace로 문자열을 바꿔놓고 하는 방법도 있다. 이게 더 보기는 편할듯?
def solution(babbling):
    answer = 0
    
    word_set = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        temp = word
        for j in range(4):
            if word_set[j] in temp:
                temp = temp.replace(word_set[j], "{0}".format(j))
        if len(temp) > 1:
            for i in range(len(temp)-1):
                if temp[i] == temp[i+1] or temp[i] not in ["0","1","2","3"]:
                    break
            else:
                if temp[-1] in ["0","1","2","3"]:
                    answer += 1
        else:
            
            if temp in ["0","1","2","3"]:
                answer += 1
    return answer