'''
0과 1로 이루어진 1차 배열에서 7개 byte(글자)를 묶어서 10진수로 출력하기

예를 들어 입력이 다음과 같다면 결과로 1, 13을 출력한다.


입력 첫 줄에 testcast의 수가 입력되고 
다음 줄 부터 testcast의 수만큼 0과 1로 이루어진 문자열이 입력된다
'''

def bin_to_dec(x):
    dec = 0
    for i in range(7):
        dec += int(x[i])*(2**(6-i))
    return str(dec)

T = int(input())
for t in range(1, T+1):
    bit_input = input()
    decimal = []
    for i in range(0, len(bit_input), 7):
        bit = bit_input[i:i+7]
        decimal.append(bin_to_dec(bit))
    print("#%d %s" %(t, ' '.join(decimal)))
    
