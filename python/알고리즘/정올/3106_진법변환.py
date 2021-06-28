# while True:
#     x = input()
#     if x == '0':
#         break
#     a,n,b = x.split()
#     decimal = int(n,int(a))
#     k = 'b' if b == '2' else 'o' if b == '8' else 'x' if b == '16' else 'd'
#     result = format(decimal, k).upper()
#     print(result)


def toChar(n):
    if n < 10:
        return str(n) + '0'
    return str(n) + chr(56)

def convert(num):
    if num < b:
        print(toChar(num))
        return
    convert(int(num/b))
    r = num % b
    print(toChar(r))

while True:
    x = input()
    if x == '0':
        break
    a,n,b = x.split()
    a = int(a)
    b = int(b)
    decimal = int(n,a)

    convert(decimal)
        