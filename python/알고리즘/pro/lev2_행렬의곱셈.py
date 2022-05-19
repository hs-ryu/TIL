def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    
    # print(answer)
    for i in range(len(answer)):
        for j in range(len(answer[0])):
            for k in range(len(arr1[0])):
                # print(i,k)
                # print(k,j)
                answer[i][j] += arr1[i][k] * arr2[k][j]
    print(answer)
    
    
    return answer