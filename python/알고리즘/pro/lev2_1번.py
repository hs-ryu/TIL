def solution(today, terms, privacies):
    answer = []

    today = list(map(int,today.split(".")))
    t = dict()
    for i in range(len(terms)):
        now_terms = terms[i].split(" ")
        t[now_terms[0]] = int(now_terms[1])
    for i in range(len(privacies)):
        now_privacies = privacies[i].split()
        day = list(map(int,now_privacies[0].split(".")))
        year = day[0]
        month = day[1]
        date = day[2]
        month += t[now_privacies[1]]
        while month > 12:
            month -= 12
            year += 1
        
        if year < today[0]:
            answer.append(i+1)
        elif year == today[0]:
            if month < today[1]:
                answer.append(i+1)
            elif month == today[1]:
                if date <= today[2]:
                    answer.append(i+1) 

    return answer