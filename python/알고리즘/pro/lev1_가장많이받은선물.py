def solution(friends, gifts):
    answer = 0
    
    sends_info = dict()
    counts_info = dict()
    will_get_counts = dict()
    
    for i in friends:
        sends_info[i] = dict()
        counts_info[i] = 0
        will_get_counts[i] = 0
    
    for i in range(len(friends)):
        for j in range(len(friends)):
            if i != j:
                sends_info[friends[i]][friends[j]] = 0
    
    for info in gifts:
        a,b = info.split(" ")
        sends_info[a][b] += 1
        counts_info[a] += 1
        counts_info[b] -= 1
    
    for i in range(len(friends)-1):
        a = friends[i]
        for j in range(i+1, len(friends)):
            b = friends[j]
            if sends_info[a][b] > sends_info[b][a]:
                will_get_counts[a] += 1
            elif sends_info[a][b] < sends_info[b][a]:
                will_get_counts[b] += 1
            elif sends_info[a][b] == sends_info[b][a]:
                if counts_info[a] > counts_info[b]:
                    will_get_counts[a] += 1
                elif counts_info[a] < counts_info[b]:
                    will_get_counts[b] += 1
                elif counts_info[a] == counts_info[b]:
                    pass
    
    # print(will_get_counts)
    answer = max(will_get_counts.values())
    
    return answer