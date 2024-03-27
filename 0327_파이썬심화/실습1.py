from math import *

def cal(a,b,c):
    d = b**2 - 4*a*c
    if d>0:
        x_p=(-b+sqrt(d))/(2*a)
        x_n=(-b-sqrt(d))/(2*a)
        print(x_p,"\n",x_n)

    if d==0:
        print("중근을 갖습니다.")
        x=(-b)/(2*a)
    
    if d<0:
        print("근이 존재하지 않습니다.")
        return 0
    
cal(2,6,2)