import sys
sys.stdin = open('input1.txt')

code_list = {'0001101' : 0, '0011001' : 1, '0010011' : 2, '0111101' : 3, '0100011' : 4, '0110001' : 5, '0101111' : 6, '0111011' : 7, '0110111' : 8, '0001011' : 9}
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    code = [input() for _ in range(N)]
    for code_line in code:
        pw = code_line.rstrip('0')
        if pw:
            decimal = []
            for i in range(len(pw) - 56, len(pw), 7):
                decimal.append(code_list.get(pw[i:i+7]))
            break
    result = (decimal[0] + decimal[2] + decimal[4] + decimal[6]) * 3 + (decimal[1] + decimal[3] + decimal[5]) + decimal[7]
    if result % 10 == 0:
        print('#%d %d' %(t, sum(decimal)))
    else:
        print('#%d %d' %(t, 0))