def check(arr, level, k):
    if level == 7:
        # print(arr)
        if sum(arr) == 100:
            for i in range(7):
                print(arr[i])
        return
    for i in range(k,9):
        arr.append(dwarf[i])
        check(arr, level+1, i+1)
        arr.pop(-1)

dwarf = []

for _ in range(9):
    dwarf.append(int(input()))

check([],0,0)