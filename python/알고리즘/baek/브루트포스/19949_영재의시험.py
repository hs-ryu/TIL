# 조합 문제?
# 1. 이미 5점 이상이면 뒤에꺼는 그냥 한번에 더해버리고 리턴해 버리는.
# 2. 5점이 안될거 같으면 그냥 리턴해버리는.
# 3. 일단 그냥 10문제 다 풀면 체크하는걸로 가자.
def search(level,correct,arr):
    # 5점 이상 맞았다면 result 증가
    if level == 10:
        if correct >= 5:
            global result
            result += 1
        return

    for i in range(1,6):
        if level >= 2:
            if arr[level-2] == arr[level-1] and arr[level-1] == i:
                continue
        arr.append(i)
        search(level+1,correct+1 if i == ans[level] else correct, arr)
        arr.pop(-1)


ans = list(map(int,input().split()))
result = 0
search(0,0,[])
print(result)