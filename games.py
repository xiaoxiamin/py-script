#!/usr/bin/env python
#coding: utf8
import random
import sys
allList = ['石头', '剪刀', '布']
gDict = {'石头':0, '剪刀':1, '布':2}
prompt = """(0)石头
(1)剪刀
(2)布
请选择对应的数字: """
chnum = raw_input(prompt)
if chnum not in '012':
    print 'Invalid choice'
    sys.exit(1)
uchoice = allList[int(chnum)]
cchoice = random.choice(allList)
#print '您选择了:', uchoice, '\n计算机选择了:',cchoice
print '您选择了: %s\n计算机选择了:%s' % (uchoice, cchoice)
if uchoice == cchoice:
    print '平局'
elif (gDict[cchoice] - gDict[uchoice] == 1) or (gDict[cchoice] - gDict[uchoice] == -2):
    print 'You WIN!!!'
else:
    print 'You LOSE!!!'
