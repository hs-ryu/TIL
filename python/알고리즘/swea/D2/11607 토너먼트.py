import sys
sys.stdin = open('sample_input.txt')

# 1. 중간점을 찾기
# 2. 두개 그룹으로 나누기
# 3. 그룹에 1개의 요소만 있으면 (나누는 작업 멈추기. = return) 자기 자신을 반환한다.
# 4. 돌아와서, 가위 바위 보 게임을 한 후, 승자를 반환.

# in DFS 함수에서
#종료 조건 : 시작점과 끝점이 같을때
# return s
#DFS 호출
# 1번 중간점 찾고
# m = (s+e) /// 2
# w1 = DFS(s,m)
# w2 = DFS(m+1, e)
# 가위바위보 게임


def gawibawibo(p1, p2):
    if x[p1] == 1 and x[p2] == 1:
        return p1
    elif x[p1] == 1 and x[p2] == 2:
        return p2
    elif x[p1] == 1 and x[p2] == 3:
        return p1
    if x[p1] == 2 and x[p2] == 1:
        return p1
    elif x[p1] == 2 and x[p2] == 2:
        return p1
    elif x[p1] == 2 and x[p2] == 3:
        return p2
    if x[p1] == 3 and x[p2] == 1:
        return p2
    elif x[p1] == 3 and x[p2] == 2:
        return p1
    elif x[p1] == 3 and x[p2] == 3:
        return p1

def game(s, e):
    if s == e:
        return s
    m = (s+e) // 2
    w1 = game(s, m)
    w2 = game(m+1, e)
    return gawibawibo(w1, w2)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    x = list(map(int, input().split()))
    s, e = 0, len(x)-1
    result = game(s, e) + 1
    print('#%d %d' % (t, result))