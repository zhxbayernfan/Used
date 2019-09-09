#!/usr/bin/env python3 
f = open('E:/Python/011/s190904.txt', 'r')
for line in f:
    print(line, end='')
f.close()
print ("1")
File = open('190904.txt', 'r')
for line in File:
    print(line, end='')
File.close()
print ("2")
File2 = open('E:/Python/011/s190801.sh', 'r')
for line in File2:
    print(line, end='')
File2.close()
print ("3")