#!/usr/bin/env python
#coding=utf-8
import urllib,re
html=urllib.urlopen("http://tieba.baidu.com/p/3999261766").read() #获取网页源码
reg=r'src="(.+?)" pic'   #正则匹配图片链接   ()里是要取的内容
reg=re.compile(reg)      #编译，可以加快匹配速度
url=re.findall(reg,html)  #整合 ，取出所有满足reg变量中 定义的内容
url.pop(21)               #这块是 有一个链接 出错了， 我给删除掉了 。
#for i,url in enumerate(url):
	#urllib.urlretrieve(url,'%s.jpg' %(i,))
for i,url in enumerate(url):   #引用ennumerate函数 ，  前边可以引用两个变量 一个是enumerate函数中元素的索引和元素内容，
	urllib.urlretrieve(url,'%s.jpg' % i)   #这个是 下载，引用urllib.urlretrieve（）方法 可以 吧下载到的图片  改名字， 刚好名字为 上边引用的元素索引 。从0开始， 到最后。
