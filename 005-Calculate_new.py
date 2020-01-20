#!/usr/bin/env python3
m = int(input("请输入一个数字: "))
n = int(input("请输入一个数字: "))
sum = 0
if m <= n:
    starter = m
    while starter <= n:
        sum = sum + starter
        starter += 1
    print("%d 到 %d 之和为: %d" % (m,n,sum))
if m > n:
    starter = n
    while starter <= m:
        sum = sum + starter
        starter += 1
    print("%d 到 %d 之和为: %d" % (n,m,sum))
