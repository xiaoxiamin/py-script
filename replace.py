#!/bin/python
#文件内容替换

import fileinput

for line in fileinput.input("simin.py",backup='bak',inplace=0,):
	line = line.replace('haha','hello')
	print line,
