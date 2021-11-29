import numpy as np
from numpy import *
import math
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import sympy as sp
def taylor(x,U,f):
    y=0
    i=0
    d=1
    y=f
    mas=[sp.diff(f,x)]
    while i <=U:
        mas.append(sp.diff(mas[i],x))
        print('mas=', i+1, '=',mas[i])
        y+=mas[i]*(x-0)**(i+1)/math.factorial(i+1)
        i+=1
    phibka=mas[i]/math.factorial(i+1)
    print ('Pohibka=',phibka)
    print ('Y=',y)
    return y
U=int(input())-1
x=sp.symbols('x')
f=(sp.sin(5*x))
taylor_x=taylor(x,U,f)
plt=sp.plot(f, taylor_x, (x,-1,1), label='Taylor')
plt.title('LB 11 Ihor Uchiha')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
