#coding=utf-8
'''
Created on 2016年12月2日

@author: lenovo
'''
import time,re

locol_time=time.ctime()

def now_time():
      return re.findall('\d+\:\d+\:\d+', time.ctime())[0]

now_month=re.findall('\w{3}', locol_time)[1]
now_day=re.findall('\d{1,2}', locol_time)[0]
#月份转数字表示
month={
       'Jan':'1',
       'Feb':'2',
       'Mar':'3',
       'Apr':'4',
       'May':'5',
       'Jun':'6',
       'Jul':'7',
       'Aug':'8',
       'Sept':'9',
       'Oct':'10',
       'Nov':'11',
       'Dec':'12'
       }
week=week_ch={
      'Mon':'周一',
      'Tues':'周二',
      'Wed':'周三',
      'Thur':'周四',
      'Fri':'周五',
      'Sat':'周六',
      'Sun':'周日'
      }
def general_time(now_time):
      if int(now_time[:2])>12:
            hour=int(now_time[:2])-12
            hour=str(hour)
      else:
            hour=now_time[:2]
      if int(now_time[3:5])>30 :
            minute="点半"
      else:
            minute="点过"
      return hour+minute
#print(locol_time,now_month,now_day,month[now_month])
#print('现在是{}月{}日的{}'.format(month[now_month],now_day,now_time[:5]),general_time(now_time))
