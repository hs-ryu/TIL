'''
16진수 문자로 이루어진 1차 배열이 주어질 때 앞에서부터 7bit씩 묶어 십진수로 변환하여 출력해 보자
예를 들어 0F97A3 이 입력일 경우 2진수로 변환하면 000011111001011110100011 이며, 7bit씩 묶어 십진수로 출력하면
0000111 1100101 1110100 011 이 되므로  7, 101, 116, 3을 출력한다
'''

hex_dic = {'0' : '0000', '1' : '0001', '2' : '0010', '3' : '0011', '4' : '0100', '5' : '0101', '6' : '0110', '7' : '0111', '8' : '1000', '9' : '1001', 'A' : '1010', 'B' : '1011', 'C' : '1100', 'D' : '1101', 'E' : '1110', 'F' : '1111'}

def bin_to_dec(x):
    dec = 0
    for i in range(len(x)):
        dec += int(x[i]) * (2**(len(x)-1-i))
    return str(dec)


T = int(input())
for t in range(1, T+1):
    hex_input = input()
    bin_str = ''
    for i in hex_input:
        bin_str += hex_dic[i]
    decimal = []
    for i in range(0,len(bin_str), 7):
        decimal.append(bin_to_dec(bin_str[i:i+7]))
    print('#%d %s' %(t, ', '.join(decimal)))

