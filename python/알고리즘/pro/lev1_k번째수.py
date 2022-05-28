def solution(array, commands):
    answer = []
    for x in range(len(commands)):
        i,j,k = commands[x]
        new_arr = array[i-1:j]
        new_arr.sort()
        answer.append(new_arr[k-1])
    return answer