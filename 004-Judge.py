#!/usr/bin/env python
c1 = 300 #300=0001 0010 1100
d1 = 91  # 91=0000 0101 1011
print ("c1的值%s\td1的值%s" % (c1,d1)) #输出多于一个变量的方法，牢记
e1 = c1 | d1 #0001 0111 1111=383
print ("e1的值为:e1=",e1) 
#实测证明，位运算不仅限于8位的二进制数（基于昨天的学习拓展）
a = 10
b = 20
if  a and b :
   print ("1-变量a和b都为 true")
else:
   print ("1-变量a和b有一个不为 true")
if  a or b :
   print ("2-变量a和b都为 true，或其中一个变量为 true")
else:
   print ("2-变量a和b都不为 true")
# 修改变量 a 的值
a = 0
if  a and b :
   print ("3-变量a和b都为 true")
else:
   print ("3-变量a和b有一个不为 true")
if  a or b :
   print ("4-变量a和b都为 true，或其中一个变量为 true")
else:
   print ("4-变量a和b都不为 true")
if not( a and b ):
   print ("5-变量a和b都为 false，或其中一个变量为 false")
else:
   print ("5-变量a和b都为 true")
c = 10
d = 20
list = [4, 8, 12, 16, 20 ]
 
if ( c in list ):
   print ("6-变量c在给定的列表中 list 中")
else:
   print ("6-变量c不在给定的列表中 list 中")
 
if ( d not in list ):
   print ("7-变量d不在给定的列表中 list 中")
else:
   print ("7-变量d在给定的列表中 list 中")
