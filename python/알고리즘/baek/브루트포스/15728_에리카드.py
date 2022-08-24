n,k = map(int,input().split())

shared = list(map(int,input().split()))
team = list(map(int,input().split()))

# 5, 2
# -1, 2, 3, 4, 5
# -1, 0, 2, 3, 4

# 방법 1. 팀 카드에서 k개의 카드를 조합으로 없애가면서, 한장씩 곱해가면서 체크한다. <- 브루트포스. 입력이 n,k의 최대값이 100이라서 가능은 할듯.
# 방법 2. 정렬 후, 앞 뒤로 없애나간다..?
shared.sort()
team.sort()

# flag가 0이면 + 값이 더 큰것. 1이라면 - 값이 더 큰것.
flag = 0
if abs(shared[0]) > abs(shared[-1]):
    flag = 1

