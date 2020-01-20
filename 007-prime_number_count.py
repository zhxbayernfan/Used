#!/usr/bin/env python3 
a = int(input("请输入一个数: "))
b = int(input("请输入一个数: "))
def mokuai (a,b):
    c = 0
    for n in range(a, b+1):
        for x in range(2, n):
            if n % x == 0:
                print(n, '等于', x, '*', n//x)
                break
        else:
        # 循环中没有找到元素
            c = c + 1
            print(n, '是从', a, '到', b, '的第', c, '个质数')
    print ("Good bye!")
if (b >= a):
    if (a >= 2):
        mokuai(a,b)
    else:
        print ("数字小于2，无输出结果。")
if (a > b):
    if (b >= 2):
        d = a
        a = b
        b = d
        mokuai(a,b)
    else:
        print ("数字小于2，无输出结果。")
