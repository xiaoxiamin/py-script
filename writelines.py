#!/bin/python
#-*- coding: UTF-8 -*-
#文件内容修改

with file('contack_list','r+') as f:
	old=f.read()
	f.seek(2)
	f.writelines("test sir say hello word!\n")

