#coding=utf-8
import re,csv

s="名字,年龄,身高"


print(re.split(',', s)[0])
print(s.split(',')[1])
