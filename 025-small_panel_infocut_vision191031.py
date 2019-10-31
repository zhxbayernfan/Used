#!/usr/bin/env python3 

import csv

File1 = open('E:/Python/025/191027_86gene_180518.csv', 'r')
for line in File1:
    print(line, end='')
File1.close()
print ("1")