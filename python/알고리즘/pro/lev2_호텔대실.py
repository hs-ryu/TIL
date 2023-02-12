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