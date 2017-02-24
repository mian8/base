import csv

s=csv.reader(open('./other/西南积分.csv','r'))
for b in s:
	if b[1]!='':
		print(b)