import numpy as np
import math
def fac(i, qq):
    j=1
    dq=1
    while j<=i:
        dq*=qq - j
        j+=1
    return dq
mas_x=[1.340,1.345,1.350,1.355,1.360,1.365,1.370,1.375,1.380,1.385,1.390]
mas_y=[4.2556 ,4.3532, 4.4552, 4.5618, 4.6734, 4.7903, 4.9130, 5.0419, 5.1774, 5.3201, 5.4706]
h = mas_x[1] - mas_x[0]
x=0.1
xo=0
xn=1.390
q=(x-xo)/h
k=0
def y(mas_y,j):
    mas=[]
    for i in range(len(mas_y)):
        mas.append(mas_y[i] - mas_y[i-1])
        
    mas.pop(0)  
    if j == 1:
        return mas
    else:
        j-=1
        return y(mas, j)
yx1=1/h*((y(mas_y, 1)[1])-(y(mas_y, 2)[1])/2+(y(mas_y, 3)[1])/3-(y(mas_y, 4)[1])/4)
yx2=1/h**2*((y(mas_y, 2)[1])-(y(mas_y, 3)[1])+11/12*(y(mas_y, 4)[1]))
q=(x-xn)/h
N_x=mas_y[0]+q*mas_y[1]-mas_y[0]
print(y(mas_y, 3))
jkl=int(input())
while k<jkl-1:
    k+=1
    N_x+=(q*(fac(k, q))/math.factorial(k+1))*(y(mas_y,k+1)[0])
N= mas_y[0] + q*mas_y[1]-mas_y[0]+(q*(q-1)/math.factorial(2))*(y(mas_y, 2)[0]) + (q*(q-1)*(q-2)/math.factorial(3))*(y(mas_y, 3)[0])
print (N_x, "Мой цыкл до 3 ----------------------------------------")
print (N, "Твоя формула до 3 -------------------------------------")



