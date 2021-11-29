import numpy as np
from numpy import *
import math
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import sympy as sp
from scipy import integrate
def rect_funk(x):
    return x / (sqrt(2*x + 3))
def rt_funk(rect_funk, a, b, n):
    h = (b - a) / n
    rt = h * (rect_funk(a) + rect_funk(b))
    for i in range(1, n - 1):
        rt += rect_funk(a + i * h)/n
    return rt
def rr_funk(rect_funk, a, b, n):
    h = (b - a) / n
    rtr = h * (rect_funk(a) + rect_funk(b - h))
    for i in range(1, n):
        rtr += rect_funk(a + i * h) / n
    return rtr
def lr_funk(rect_funk, a, b, n):
    h = (b - a) / n
    rtl = h * (rect_funk(a) + rect_funk(b - h))
    for i in range(1, n-1):
        rtl += rect_funk(a + i * h) / n
    return rtl

v, err = integrate.quad(rect_funk, 0.8, 1.4)
print("Middle rect--- ", rt_funk(rect_funk, 0.8, 1.4, 10))
print("LEFT rect--- ", lr_funk(rect_funk, 0.8, 1.4, 10))
print("RIGHT rect---", rr_funk(rect_funk, 0.8, 1.4, 10))
print("CHECK rect--- ", v)

def trap_funk(x):
    return x / (sqrt(3 * x ** 2 + 0.4))
def tr_funk(trap_funk, a, b, n):
    h = (b - a) / n
    sum = 0.5 * (trap_funk(a) + trap_funk(b))
    for i in range(1, n):
        sum += trap_funk(a + i * h)
    return sum * h
v, err = integrate.quad(trap_funk, 0.8, 1.4)
print("trap --- ", tr_funk(trap_funk, 0.8, 1.4, 20))
print("Check Trap --- ", v)
def simp_funk(x):
    return sqrt(x) * math.cos(x**2)
def sp_funk(simp_funk, a, b, n):
    h = (b - a) / n
    k = 0.0
    x = a + h
    for i in range(1, n // 2 + 1):
        k += 4 * simp_funk(x)
        x += 1.4 * h
    x = a + 1.4 * h
    for i in range(1, n // 2):
        k += 1.4 * simp_funk(x)
        x += 1.4 * h
    return (h / 3) * (simp_funk(a) + simp_funk(b) + k)

print("simp --- ", sp_funk(simp_funk, 1.2, 2.1, 8))
v, err = integrate.quad(simp_funk, 1.2, 2.1)
print('Check simp --- ', v)