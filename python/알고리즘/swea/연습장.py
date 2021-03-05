# import sys
# sys.stdin = open('sample_input2.txt')

''' 문제 1 : 문자열
def brout_force1(p,t):
    for i in range(len(t) - len(p) + 1):
        for j in range(len(p)):
            if p[j] == t[i+j]:
                break
        else:
            return 1
    return 0

def brout_force2(p,t):
    i = 0
    j = 0
    
    while j < len(p) and i < len(t):
        if p[j] != t[i]:
            i = i-j
            j = -1
        i += 1
        j += 1
    if j == len(p): return 1
    else: return 0
    

T = int(input())
for t in range(1, T+1):
    str1 = input()
    str2 = input()


'''

''' 회문
def my_reverse(line):
    r_line = []
    # 뒤에서부터 읽어오면서 뒤집은 리스트 만들기
    for i in range(len(line)-1, -1, -1):
        r_line.append(line[i])
    return r_line

def my_find():
    for i in range(N):
        # 가로
        for j in range(N-M+1):
            # 부분 문자열을 위한 빈리스트
            tmp = []
            # 부분 물자열 완선
            for k in range(M):
                tmp.append(words[i][j+k])
            # 회문검사
            if tmp == my_reverse(tmp):
                return tmp
        # 세로
        for j in range(N-M+1):
            tmp = []
            for k in range(M):
                tmp.append(words[j+k][i])
            if tmp == my_reverse(tmp):
                return tmp
    # 만약 회문이 없으면
    return []

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())

    words = [list(input()) for _ in range(N)]

    ans = my_find()

    print(''.join(ans))
'''

'''과제회문
def my_find(M):
    #전체 크기가 N이다.
    for i in range(N):
        #부분 문자열의 시작점
        for j in range(N-M+1):
            #스왑을 응용한 회문검사
            #가로검사
            for k in range(M//2):
                #앞뒤 검사
                if words[i][j+k] != words[i][j+M-1-k]:
                    break
                #회문이다
                elif k == M//2 - 1 :
                    return M
            #세로검사
            for k in range(M//2):
                if words[j+k][i] != words[j+M-1-k][i]:
                    break
                elif k == M//2 - 1:
                    return M
                
    return 0

for t in range(1, 11):
    T = int(input())
    N = 100

    words = [input() for i in range(N)]

    #가장 길이가 긴거부터 회문검사를 한다.
    for i in range(N, 0, -1):
        ans = my_find(i)
        
        if ans != :
            break
    print(ans)
'''

'''글자수
T = int(input())
for t in range(1, T+1):
    
    str1 = input()
    str2 = input()
    
    # str1 각 문자의 카운트를 세기 위함
    cnt = [0] * len(str1)
    
    # str1의 길이만큼 순회
    for i in range(len(str1)):
        # str1[i]가 str2에 몇개 들어있는지 체크
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                cnt[i] += 1
                
    ans = 0
    # 가장 큰 값 찾기
    for i in range(len(cnt)):
        if ans < cnt[i]:
            ans = cnt[i]
            
    # ans = max(cnt)
    print(ans)
'''

'''글자수 (딕셔너리 사용)
T = int(input())
for t in range(1, T+1):
    str1 = input()
    str2 = input()
    
    # 키 = 문자, value = 카운트한 수
    my_dict = {}
    
    for key in set(str1):
        my_dict[key] = 0
    
    for key in str2:
        if key in my_dict:
            my_dict[key] += 1
            
    ans = 0
    
    for i in my_dict.values():
        if ans < i:
            ans = i
'''


''' 낱말 퍼즐
T = int(input())
for t in range(1, T+1):
    # N : 2차원 리스트 크기, K : 내가 원하는 길이
    N, K = map(int,input().split())

    # 리스트 내포 방식을 활용한 입력
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    for i in range(N):
        cnt = 0
        #행을 검사
        for j in range(N):
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0 or j == N-1:
                # 벽을 만났을 때 그동안 쌓아온 cnt 값이 K이면 들어갈 수 있다.
                if cnt == K:
                    ans += 1
                cnt = 0
        #열을 검사
        for j in range(N):
            if puzzle[j][i] == 1:
                cnt += 1
            if puzzle[j][i] == 0 or j == N-1:
                if cnt == K:
                    ans += 1
                cnt = 0

    print('#%d %d' %(t,ans))
'''

''' 낱말퍼즐 다른 방식 (오른쪽, 아래에 벽 두르기)
T = int(input())
for t in range(1, T+1):
    # N : 2차원 리스트 크기, K : 내가 원하는 길이
    N, K = map(int,input().split())

    puzzle = [list(map(int,input().split())) + [0] for _ in range(N)]
    puzzle.append([0]*(N+1))

    ans = 0

    for i in range(N):
        cnt = 0
        # 벽을 한칸 더 둘렀기 때문에 1 증가시킨 범위까지 확인.
        for j in range(N+1):
            if puzzle[i][j]:
                cnt+=1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0

        for j in range(N+1):
            if puzzle[j][i]:
                cnt += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0

'''


''' 세로로 출력하기
T = int(input())
for t in range(1, T+1):
    word = [0] * 5
    # 최대길이를 담을 값
    max_len = 0

    for i in range(5):
        word[i] = list(input())

        # 입력을 받으면서 최대 길이를 갱신
        if len(word[i]) > max_len:
            max_len = len(word[i])

    #세로로 읽기
    for i in range(max_len):
        for j in range(5):
            # if len(word[j]) > i:
            #     print(word[j][i], end='')
            try:
                print(word[j][i], end='')
            except:
                pass
    print()
'''


'''쇠막대 짜르기
T = int(input())
for t in range(1, T+1):
    iron_bar = input()

    cnt = 0 #막대수
    ans = 0 #정답

    for i in range(len(iron_bar)):
        #열린 괄호라면 막대 추가
        if iron_bar[i] == '(':
            cnt += 1
        else:
            # 닫힌 괄호라면 막대 감소
            # 레이져라면 당연히 잘못 세었으니까 빼는게 맞다
            # 아니라면 어차피 철봉 끝이니 빼줘야한다.
            cnt -= 1
            # 레이져
            if iron_bar[i-1] == ')':
                # 레이저로 인해서 잘린 막대들이 생겼으므로
                ans += cnt
            else:
                # 막대 끝이라는 뜻.
                ans += 1
    print(ans)
'''


''' powerset(모든 부분집합들) 재귀방식으로 구하기
N = 3   # input
arr = [1, 2, 3]   # 우리가 활용할 데이터
sel = [0] * N  # a 리스트(내가 해당 원소를 뽑았는지 체크)

def powerset(idx):
    if idx == N:
        print(sel, ":", end=" ")
        for i in range(N):
            if sel[i]:
                print(arr[i], end=' ')
        print()
        return

    # idx 자리의 원소를 뽑고 간다.
    sel[idx] = 1 # True
    powerset(idx + 1)

    # idx 자리의 원소를 안 뽑고 간다.
    sel[idx] = 0    # False
    powerset(idx + 1)

powerset(0)
'''


'''  순열 재귀
arr = [1, 2, 3]
N = 3
sel = [0] * N # 결과들이 저장될 리스트
check = [0] * N #해당 원소를 이미 사용 했는지 안했는지에 대한 체크

def perm(idx):
    #다 뽑아서 정리했다면
    if idx == N:
        print(sel)
    else:
        for i in range(N):
            if check[i] == 0:
                sel[idx] = arr[i]   # 값을 써라
                check[i] = 1    # 사용을 했다는 표시
                perm(idx+1)
                check[i] = 0    # 다음 반복문을 위한 원상복구

perm(0)
'''

''' 순열 비트 (동작과정 손으로 한번 해보기)
arr = [1, 2, 3]
N = 3
sel = [0] * N   # 뽑은 결과를 적음

# check : 10진수 정수
def perm(idx, check):
    if idx == N:
        print(sel)
        return
    for j in range(N):
        #j번째 원소를 이미 활용 했군. 그럼 쓰면 안되지.
        if check & (1 << j):
            continue
        sel[idx] = arr[j]
        perm(idx+1, check | (1 << j)) #원상복구 과정 필요없다.

perm(0, 0)
'''

''' 순열 스왑
arr = [1, 2, 3]
N = 3

def perm(idx):
    if idx == N:
        print(arr)
        return
    for i in range(idx, N):
        arr[idx], arr[i] = arr[i], arr[idx]
        perm(idx+1)
        arr[idx], arr[i] = arr[i], arr[idx]
perm(0)
'''

# 반복문을 이용한 선형시간 O(n)

'''거듭제곱(분할 정복)
def Iterative_power(x, n):
    result = 1
    for i in range(1, n+1):
        result *= x
    return result

# 분할 정복을 이용한 선형시간 O(logn)
def Recursive_power(x, n):
    if n == 1:
        return x
    if n % 2 == 0:
        y = Recursive_power(x, n//2)
        return y*y
    else:
        y = Recursive_power(x, (n-1)//2)
        return y*y*x
'''

''' 마이츄 문제
N = 20 # 마이츄 개수

queue = [(1,0)]  # 초기화
# (0,0) [0] : 사람 번호, [1] : 직전까지 받았던 마이츄의 개수

new_people = 1
last_people = 0

while N > 0 :
    num, cnt = queue.pop(0)     # 받으러온 사람, 저번까지 받은 개수

    last_people = num   # 마지막으로 받으러 온 사람
    cnt += 1    # 저번보다는 하나더 챙겨가자

    N -= cnt    # num 이라는 치구가 cnt 개수만큼 가져감.
    new_people += 1

    queue.append((num, cnt))     # 맨 뒤로 가서 다시 줄 섬
    queue.append((new_people, 0))   # 새로운 사람도 줄 섬
    print(queue)
print(last_people)
'''

'''
a = ['배', '감', '귤']
n = 3
k = 3

for i in range(n): #중복 허용
    for j in range(i, n):
        for k in range(j, n):
            print(a[i], a[j], a[k])

a = ['배', '감', '귤']
n = 3
k = 3

x = [0, 0, 0]
idx = 0
def bubun(level, m): #중복 허용
    global idx
    if level == k:
        print(x)
        return
    for i in range(m, n):
        x[level] = a[i]
        bubun(level+1, i)
bubun(0, 0)
'''