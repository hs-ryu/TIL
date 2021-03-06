'''
문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
'''

'''
입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
'''



st = input().upper()     #인풋 받아서 대문자로(소문자로 하려면 lower())
dic = {chr(i) : 0 for i in range(65,91)}   #A~Z를 키값으로 가지는 딕셔너리 생성. 모든 value는 0으로 설정해놈.
for i in st:   #반복문을 통해, 입력받은 문자열의 문자에 해당하는 딕셔너리 value를 1씩 증가시킴
    dic[f"{i}"] += 1
dic2 = sorted(dic.items(),reverse = True, key = lambda x : x[1])  #딕셔너리를 key값에 따라 정렬함. 이때, dic2는 리스트로 변경됨.
if dic2[0][1] == dic2[1][1]:   #만약 정렬된 dic의 첫번째값의 value와 두번째 값의 value가 같다면(최대값이 2개라면)
    print("?")  #물음표 출력
else:  #최대값이 1개밖에 없을땐?
    print(dic2[0][0])   #그놈 출력