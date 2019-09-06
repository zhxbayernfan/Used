#!/usr/bin/env python3 
def fib(n):    # 定义到 n 的斐波那契数列
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()
 
def fib2(n): # 返回到 n 的斐波那契数列
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
n = int(input("请输入一个数n: "))
print ("到数字",n,"的斐波那契数列结果为")
fib(n)
print ("返回到数字",n,"的斐波那契数列结果为",fib2(n))