from copy import deepcopy

def search(arr, level, k):
    if level == 7:
        total = sum(arr)
        if total == 100:
            global result
            result = deepcopy(arr)
            return

    for i in range(k, 9):
        arr.append(dwarf[i])
        search(arr,level+1,i+1)
        arr.pop()

dwarf = []
for i in range(9):
    dwarf.append(int(input()))
result = []
search([],0,0)
result.sort()
for i in range(7):
    print(result[i])