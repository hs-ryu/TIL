# 4 2 8 9 
# 2 4 8 9

# 1개씩
# 2, 4, 8, 9 => 23

# 2개씩
# 2, 4 => 8
# 8, 9 => 17
# => 25

# 2, 8 => 16
# 4, 9 => 18
# 34 답

# 2, 4 => 8
# 8, 9 => 18
# 26

# 2 9 => 18
# 4 8 => 16
# 34 답

# 2개 1개 1개
# 2, 4 => 8
# 25

# 2, 8 => 16
# 29

# 2, 9 => 18
# 30

# 4, 8 => 16
# 27

# 4, 9 => 18
# 28

# 8, 9 => 18
# 24

# 3개 1개
# 2,4,8 => 12
# 21

# 2,4,9 => 12
# 20

# 2,8,9 => 24
# 28

# 4,8,9 => 24
# 26

# 4개
# 2,4,8,9 => 32

# 2개씩, 정렬해놓고 왼쪽 오른쪽 하나씩 넣으면 될듯

n = int(input())
cow = list(map(int,input().split()))
cow.sort()

result = 0
length = len(cow)
while length >= 2:
    # print(cow)
    a = cow.pop(0)
    b = cow.pop(-1)
    result += b * 2
    length = len(cow)

if len(cow) == 1:
    result += cow[0]
    print(result)
else:
    print(result)