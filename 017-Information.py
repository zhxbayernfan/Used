#!/usr/bin/env python3
import csv

headers = ['Number','Name','Year_of_Birth','Nationality','Position','Last_Team']

rows = [
        [1,'xaoming','male',168,23],
        [1,'xiaohong','female',162,22],
        [2,'xiaozhang','female',163,21],
        [2,'xiaoli','male',158,21]
    ]

with open('E:/python/017/test.csv','w',newline='')as file1:
    file1_csv = csv.writer(file1)
    file1_csv.writerow(headers)
    file1_csv.writerows(rows)
