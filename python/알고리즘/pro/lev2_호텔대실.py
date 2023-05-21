# 음.. 테스트케이스는 다 맞는데 왜 정답이 아닐까....
# 고민해보자

def solution(book_time):
    answer = 0
    book_time.sort(key=lambda x:(int(x[0][:2]),int(x[0][3:5])))
    rooms = []
    
    for i in range(len(book_time)):
        temp = book_time[i]
        if len(rooms) == 0:
            rooms.append(temp)
        else:
            flag = 0
            for i in range(len(rooms)):
                check_room = rooms[i]
                start = list(map(int,temp[0].split(":")))
                end = list(map(int,temp[1].split(":")))
                exist_start = list(map(int,check_room[0].split(":")))
                exist_end = list(map(int,check_room[1].split(":")))
                
                time1 = start[0] * 60 + start[1]
                time2 = exist_end[0] * 60 + exist_end[1]
                
                if time2 + 10 <= time1:
                    flag = 1
                    break
            if flag == 1:
                rooms[i] = check_room
            else:
                rooms.append(temp)
                
                
    return len(rooms)

# 딱히 하나씩 비교할 필요가 없다.
# 시작 시간과, 끝나는 시간을 하나의 배열로 정리하고, 시간에 따라 정렬을 해서 하나씩 확인하면 된다.
# 하나의 시간을 골랐을 때 입실 시간이라면 -> 그 다음에 또 입실 시간이 들어오면 방을 하나 추가해야하고, 퇴실 시간 + 10분 이 들어오면 하나 줄인다.
# 근데 그냥 줄이면, 끝났을때 나중에 몇개의 방이 생겼을지 모르기 때문에 반복 하나 돌때마다 계속해서 answer 값을 갱신해줘야한다.
def solution(book_time):
    answer = 0
    book_time_int=[]

    for start,end in book_time:
        book_time_int.append([int(start[:2])*60+int(start[3:]),1])
        book_time_int.append([int(end[:2])*60+int(end[3:])+10,0])
    # print(book_time_int)
    book_time_int.sort()

    now=0
    for time in book_time_int:
        if time[1]==1:
            now+=1
        else:
            now-=1
        answer=max(answer,now)

    return answer