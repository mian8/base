#coding=utf-8
from xml.dom import minidom
import os
#打开XML文件
mes=minidom.parse('./other/TEST-AppCrawler_0.xml')

#获取文档对象
element=mes.documentElement

#根据tagname获取对象
tag=mes.getElementsByTagName('property')
#tag=element.getElementsByTagName(property)

#定位text标签
values=mes.getElementsByTagName('text')
#获取标签信息
print(mes.documentElement.nodeName)
#获取标签对属性
print(mes.getElementsByTagName('property')[3].getAttribute('name'))
print(tag[3].getAttribute('name'))
#获取标签对的值
print(values[0].firstChild.data)