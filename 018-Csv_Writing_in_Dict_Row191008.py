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
#信息收集
print('Number:%s \nName:%s \nYear_of_Birth:%s'%(Number,Name,Year_of_Birth))
print('Nationality:%s \nPosition:%s \nLast_Team_before_Bayern:%s \nWith_·_Now:%s'%(Nationality,Position,Last_Team_before_Bayern,With_·_Now))
#print到终端作为一次检查，如果出错及时更正
rows = [
        ['01','Manuel Neuer','1988','Deutsch','GK','Shalke04',''],
        ['04','Nikolas Sule','1995','Deutsch','CB','Hoffinheim',''],
        ['05','Benjamin Pavard','1996','France','CB','Stuttgart',''],
        ["05·",'Mats Hummels','1988','Deutsch','CB','Dortmund','Dortmund']
    ]
#默认row
new_row = [Number, Name, Year_of_Birth, Nationality, Position, Last_Team_before_Bayern, With_·_Now]  
#  把所有元素直接塞进这个list里
rows.append(new_row)  
#  每次在程序中输入完一行，就把新建的一个项(new_row)加入到rows中，最后再在下面的with处理段写入文件。
with open('E:/python/018/testing.csv','w',newline='')as file1:  
    file1_csv = csv.writer(file1)
    file1_csv.writerow(headers)
    file1_csv.writerows(rows)
#csv写入
