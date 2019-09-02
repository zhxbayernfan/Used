#!/usr/bin/env python3 
class demo:
    name = ""
    def _init_(self):
        self.ex()
        self.start()
    def inputName(self):
        global name
        name = input("输入您的姓名：")
    def getFirstName(self):
        if len(name) <= 0:
            x = "别闹！請输入姓名！"
            return x
        else:
            x = name[0]
            return x
    def getLastName(self):
        if len(name) <= 1:
            y = "别闹！长度不够！"
            return y
        else:
            y = name[1:]
            return y
myname = demo()
myname.inputName()
print("您的姓氏是",myname.getFirstName())
print("您的名字是",myname.getLastName())