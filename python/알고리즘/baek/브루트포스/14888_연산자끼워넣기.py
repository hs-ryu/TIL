

calc_list = ['+','-','*','//']





def search(level, arr):
    # print(arr)
    if level == n-1:
        global min_num, max_num
        res = 0
        i = 0

        new_arr = [''] * (2*n-1)
        for j in range(2*n-1):
            new_arr[j] = arr[j]

        
        while len(new_arr) != 1:
            if i % 2:
                a = new_arr[i-1]
                c = new_arr[i]
                b = new_arr[i+1]

                if c == '//':
                    if int(a) < 0 and int(b) > 0:
                        a = '-' + a
                        s = eval(a+c+b)
                        s *= (-1)
                    else:
                        s = eval(a+c+b)
                else:
                    s = eval(a+c+b)

                i = 0
                new_arr.pop(i)
                new_arr.pop(i)
                new_arr.pop(i)
                new_arr.insert(0,str(s))
            i += 1
        # print(new_arr)
        res = int(new_arr[0])
        if res > max_num:
            max_num = res
        if res < min_num:
            min_num = res
        return
    
    for i in range(4):
        if calc[i]:
            calc[i] -= 1
            c = calc_list[i]
            arr.insert(2*level+1, c)
            search(level+1, arr)
            arr.pop(2*level+1)
            calc[i] += 1
            
n = int(input())
a = list(input().split())
calc = list(map(int,input().split()))

min_num = 1000000001
max_num = -1000000001

search(0,a)

print(max_num)
print(min_num)