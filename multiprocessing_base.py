import os,multiprocessing
import base_time,time,random
#进程
'''
def first():
	print('os.getpid1 %s'%os.getpid())

if __name__=='__main__':
	print('os.getpid2 %s'%os.getpid())
	p=multiprocessing.Process(target=first,args=())
	print('???')
	p.start()
	p.join()
	print('!!!')
'''
def long_time_task(name):
	print('进程%s的ID：%s'%(name,os.getpid()))
	start = base_time.now_time()
	time.sleep(random.random()*3)
	end=base_time.now_time()
	print('任务%s执行了%0.2f秒'%(name,int(end[-2:])-int(start[-2:])))


if __name__=='__main__':
	print('父进程ID：%s'%os.getpid())
	p=multiprocessing.Pool(4)
	for  i in range(6):
		p.apply_async(long_time_task,args=(i,))
	p.close()
	p.join()
	print('执行结束')