#!/usr/bin/env python3
import math
a = int (input('请输入一个数:'))
b = int (input('请输入一个数:'))
def power1(x):
    return x * x
print (a,'的平方为',power1(a))
def power2(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print (a,'的',b,'次方为',power2(a,b))
def power3(x,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print (a,'的 2 次幂为',power3(a),'未输入b,默认为2')
print (a,'的',b,'次幂为',power3(a,b))
