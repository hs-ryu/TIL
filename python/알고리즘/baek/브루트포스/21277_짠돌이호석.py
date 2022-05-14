# 겹쳐서, 안되면 1칸 오른쪽으로 보내보고, 밑으로도 1칸 보내보고 다 보내보기.
# 돌려서 똑같이 작업 ㄱ


# 돌려돌려 돌림판
def turn(arr):
    r = len(arr)
    c = len(arr[0])
    new_arr = [[0 for _ in range(r)] for _ in range(c)]
    r,c = c,r
    for i in range(r):
        for j in range(c):
            new_arr[i][j] = arr[c-1-j][i]
    return new_arr

n1, m1 = map(int,input().split())
puzzle1 = [list(map(int,list(input()))) for _ in range(n1)]
n2, m2 = map(int,input().split())
puzzle2 = [list(map(int,list(input()))) for _ in range(n2)]


# for i in range(n2):

max_r = 0
max_c = 0

puzzle_pan = puzzle1[:]

# 4중 포문 600 만번

# for i in range(n1):
#     for j in range(m2):


print(puzzle_pan)


