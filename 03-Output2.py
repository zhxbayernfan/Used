#!/usr/bin/env python
a=121 #121= 0111 1001
b=11  
c=a/b
print ("c的值为:c=",c)
print ("a的值%s\tb的值%s" % (a,b))
d=91
print ("d的值为:d=",d)   #91= 0101 1011
e1=a&d #0101 1001=89
print ("e1的值为:e1=",e1) 
e2=a|d #0111 1011=123
print ("e2的值为:e2=",e2)
e3=a^d #0010 0010=34
print ("e3的值为:e3=",e3)
e4=e3<<1 #0100 0100=68
print ("e4的值为:e4=",e4)
e5=e3<<2 #1000 1000=136
print ("e5的值为:e5=",e5)
e6=e3>>1 #0001 0001=17
print ("e6的值为:e6=",e6)