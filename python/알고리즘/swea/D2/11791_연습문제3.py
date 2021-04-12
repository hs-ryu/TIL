'''
16진수 문자로 이루어진 1차 배열이 주어질 때 암호비트패턴을 찾아 차례대로 출력하시오. 암호는 연속되어있다.
예를 들어 0DEC 인 경우 00 001101 111011 00 으로 해석되어 0, 2 가 출력된다.
'''

code = ['001101', '010011', '111011', '110001', '100011', '110111', '001011', '111101', '011001', '101111']

def hex_to_bin(x):
    return format(int(i,16),'b').zfill(4)


T = int(input())
for t in range(1, T+1):
    hexa_input = input()
    bin_str = ''
    for i in hexa_input:
        bin_str += hex_to_bin(i)
    
    for i in range(len(bin_str)):
        if bin_str[i:i+6] in code:
            new_bin_str = bin_str[i:]
            break
    result = []
    for i in range(len(new_bin_str)//6):
        result.append(str(code.index(new_bin_str[i*6:i*6+6])))
    print('#%d %s' %(t, ', '.join(result)))