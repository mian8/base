from time import sleep,ctime
from base_time import now_time
import threading
#线程
def first(thing,times):
	for i in range(times):
		print('第一步%s%s'%(thing,now_time()))
		sleep(3)

def second(thing,times):
	for i in range(times):
		print('第二步%s%s'%(thing,now_time()))
		sleep(4)

threads=[]
'''
t1=threading.Thread(target=first,args=('吃饭',3))
t2=threading.Thread(target=second,args=('睡觉',2))
threads.append(t1)
threads.append(t2)
'''
def third(file_,time):
	for i in range(2):
		print('第三步%s%s'%(file_,now_time()))
		sleep(time)

lists={'玩游戏':3,'写代码':4,'发发呆':7}
files=range(len(lists))

for file_,times in lists.items():
	t=threading.Thread(target=third,args=(file_,times))
	threads.append(t)

if __name__=='__main__':
	print('开始走%s'%now_time())
	for t in files:
		threads[t].start()
	for t in files:
		threads[t].join()
	print('运行完%s'%now_time())
