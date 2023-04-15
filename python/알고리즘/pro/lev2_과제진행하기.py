def solution(plans):
    answer = []
    
    # 배열이 시간순으로 정렬되어 있지 않을 수 있기 때문에, 정렬 한번 해준다.
    plans.sort(key=lambda x: (int(x[1][:2]), int(x[1][3:])))
    
    stack = []
    for i in range(len(plans)-1):
        next_plan = plans[i+1]
        now_plan = plans[i]
        # 시간 계산 귀찮으니, 분으로 계산하자.
        next_time = int(next_plan[1][:2]) * 60 + int(next_plan[1][3:])
        # 현재 작업을 작업 스택에 넣어준다.
        now_time = int(now_plan[1][:2]) * 60 + int(now_plan[1][3:])
        stack.append([now_plan[0], now_time, int(now_plan[2])])
        
        # 다음 작업 시작 전까지, 스택에 담긴 작업을 끝낼 수 있는지 확인한다. 현재 작업도 stack에 넣고 시작하기 때문에 현재 작업부터 볼 것임.
        while stack:
            temp_plan = stack.pop(-1)
            temp_obj = temp_plan[0]
            temp_time = temp_plan[1] # 얜 필요 없긴 함. 그래도 폼 안꼬이게 맞춰주자.
            temp_limit = temp_plan[2]
            # 현재 시간 기준으로 다음 시간 이전에 끝내는게 가능하다면? 끝낸다. 
            if now_time + temp_limit <= next_time:
                answer.append(temp_obj)
                # now_time 업데이트 시켜주자. 그래야 stack에 남은 작업들도 시도 해볼테니까.
                now_time += temp_limit
            # 불가능하다면? stack에 다시 추가해주고 break. 남은 시간 업데이트 해서 넣어줘야함.
            else:
                stack.append([temp_obj,temp_time,now_time + temp_limit - next_time])
                break
    # 마지막 작업은 아직 계산 안됐으니까, 따로 넣어주기. 또, stack에서 하나하나 빼서 넣어주는 작업 해줘야함.
    answer.append(next_plan[0])
    while stack:
        temp_plan = stack.pop(-1)
        answer.append(temp_plan[0])
    
    return answer