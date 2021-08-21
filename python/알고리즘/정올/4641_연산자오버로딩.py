class rectangle():
    def area(self,r,c):
        return r*c

r1, c1 = map(int,input().split())
r2, c2 = map(int,input().split())

rect = rectangle()
if rect.area(r1,c1) < rect.area(r2,c2):
    print('a is smaller')
else:
    print('b is smaller')

