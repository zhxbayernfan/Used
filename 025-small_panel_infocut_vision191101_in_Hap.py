#!/usr/bin/env python3 

import csv

File1 = open('E:/Python/025/191027_86gene_180518.csv', 'r')
for line in File1:
    print(line, end='')
File1.close()
print ("1")
#1从上机信息表抓出探针为86gene_180518的横行，即小panel
#后续将地址改到x02:/haplox/users/zhanghx/103working/ 专门建立一个文件夹收集每期下机数据中的小panel成分

#2从X列获取产品关键信息并建立一一对应关系（X列中关键字~文件夹中对应获取的关键字）
#①11~lung11 ②90~lung90 ③51~stomach51 ④37~breast37 ⑤BRCA~breast2~BRCA1/2 ⑥2~gist2（此处考虑中文对应 不然会与BRCA产生交混）

#3进入x02:/haplox/rawout/对应文件夹下，运行环境为下机整批文件夹目录下 去翻YB代码YS代码参考

#4以一一对应关系找到对应文件

#5包成对应文件夹下的目录，文件夹命名“dataID+产品名”