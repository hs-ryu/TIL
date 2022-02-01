# from sys import stdin
# input = stdin.readlines

while True:
    s = input()
    if s == "END":
        break
    s = list(s)
    s.reverse()
    print("".join(s))


# 참고
# a = [1,2,3,4,5]
# b = ['a','b','c']
# 아래는 None
# print(a.reverse())
# print(b.reverse())

# 바로 프린트 하면 안됨. 아래처럼 써야함.
# a.reverse()
# print(a)
