# 조합. 다 조합해보기
def check(level, arr):
    if level == n:
        # print(arr)
        global possible_songs
        visited = [0] * m
        temps = arr[:]
        # 하나씩 꺼내서 체크
        while temps:
            temp = temps.pop(0)
            possible_song = possibles[temp]
            for i in range(m):
                if possible_song[i] == "Y":
                    visited[i] = 1
        cnt = visited.count(1)
        if possible_songs <= cnt:
            possible_songs = cnt
            global result
            result = min(result, len(arr))
        return

    arr.append(guitars[level])
    check(level+1, arr)
    arr.pop(-1)
    check(level+1, arr)

n,m = map(int,input().split())


guitars = []
songs = []
possibles = dict()

result = 51
possible_songs = 0
for _ in range(n):
    guitar, possible = input().split()
    guitars.append(guitar)
    songs.append(possible)
    possibles[guitar] = possible

check(0,[])
print(result if result else -1)