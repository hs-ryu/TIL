n = int(input())

def hanoi(i,s,e,t):
    if i == 1:
        print(f"1 : {s} -> {e}")
    else:
        hanoi(i-1, s, t, e)
        print(f"{i} : {s} -> {e}")
        hanoi(i-1, t, e, s)

hanoi(n,1,3,2)