# from sys import stdin
# input = stdin.readline

now = list(map(int,input().split(":")))
natrumn = list(map(int,input().split(":")))
# print(now)

if now[0] > natrumn[0]:
    natrumn[0] += 24

second = natrumn[2] - now[2]
if second < 0:
    second += 60
    natrumn[1] -= 1
minute = natrumn[1] - now[1]
if minute < 0:
    minute += 60
    natrumn[0] -= 1
hour = natrumn[0] - now[0]

# 최초 1초 기다려야함. 즉, 터지는 시간이 같으면 하루 뒤를 말하는거임.
if (hour == 0 and minute == 0 and second == 0):
    hour = 24

result = [str(hour), str(minute), str(second)]
for i in range(3):
    if len(result[i]) < 2:
        result[i] = '0' + result[i]
print(':'.join(result))