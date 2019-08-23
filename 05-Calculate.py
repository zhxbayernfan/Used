#!/usr/bin/env python3
n = int(input("请输入一个数字: "))
m = int(input("请输入一个数字: "))
sum = 0
counter = m
while counter <= n:
    sum = sum + counter
    counter += 1
 
print("%d 到 %d 之和为: %d" % (m,n,sum))