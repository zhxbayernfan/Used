#!/usr/bin/env python3
import csv
headers = ['Number','Name','Year_of_Birth','Nationality','Position','Last_Team_before_Bayern',"With_·_Now"]

print('Please Enter Player Information:')
Number = str(input('请输入号码:'))
Name = str(input('请输入名字:'))
Year_of_Birth = str(input('请输入出生年份:'))
Nationality = str(input('请输入国籍:'))
Position = str(input('请输入位置:'))
Last_Team_before_Bayern = str(input('前一支球队:'))
With_·_Now = str(input('带有·的现在所在何处:'))

print('Number:%s \nName:%s \nYear_of_Birth:%s'%(Number,Name,Year_of_Birth))
print('Nationality:%s \nLast_Team_before_Bayern:%s \nWith_·_Now:%s'%(Nationality,Last_Team_before_Bayern,With_·_Now))

row = {'Number':Number,'Name':Name,'Year_of_Birth':Year_of_Birth,'Nationality':Nationality,'Position':Position,'Last_Team_before_Bayern':Last_Team_before_Bayern,'With_·_Now':With_·_Now}
print (row)

rows = [
        ['01','Manuel Neuer','1988','Deutsch','GK','Shalke04',''],
        ['04','Nikolas Sule','1995','Deutsch','CB','Hoffinheim',''],
        ['05','Benjamin Pavard','1996','France','CB','Stuttgart',''],
        ["05·",'Mats Hummels','1988','Deutsch','CB','Dortmund','Dortmund']
    ]

with open('E:/python/018/testing.csv','w',newline='')as file1:  
    file1_csv = csv.writer(file1)
    file1_csv.writerow(headers)
    file1_csv.writerows(rows)

