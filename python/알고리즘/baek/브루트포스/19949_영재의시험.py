# 조합 문제?
# 1. 이미 5점 이상이면 뒤에꺼는 그냥 한번에 더해버리고 리턴해 버리는.
# 2. 5점이 안될거 같으면 그냥 리턴해버리는.
def search(level,correct,arr):
    # 5점 이상 맞았다면 result 증가
    if correct >= 5:
        global result
        result += 1
    if level == 10:
        return

    for i in range(1,6):
        arr.append(i)
        search(level+1,correct, arr)
        arr.pop(-1)

    
    pass



ans = list(map(int,input().split()))
result = 0
search()