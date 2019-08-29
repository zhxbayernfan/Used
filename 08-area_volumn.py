#!/usr/bin/env python3 
π = 3.14
def area(r):
    area = r * r * π
    return area 

def volumn(r, h):
    volumn = r * r * π * h / 3
    return volumn

r = int(input("请输入底面半径: "))
h = float(input("请输入高: "))
print('底面半径为', r, '高为', h, '的圆锥体，底面积为', area(r),'体积为', volumn(r, h))