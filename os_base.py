import os
import time
def changname(y,z):#修改名字y为z,且保存y,z
	os.rename(y,z)
	x=y+','+z
	with open('./other/name.txt','w+') as f:
		f.write(x)

def backname():#取出保存的y,z交换
	with open('./other/name.txt','r')as f:
		x=f.readline()
	y=x.split(',')[0]
	z=x.split(',')[1]
	os.rename(z,y)


#changname('./other/xueqiu.yml', './other/xueqiu.xml')
#time.sleep(5)
#backname()