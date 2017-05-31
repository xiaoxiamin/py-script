#!/bin/python

fl=open("test.txt","r+")
txt=fl.readlines()
fl.close()
a=[]

for i in txt:
	txt_list = i.replace("\n","").split(" ")
	txt_list1 = txt_list[1].split(".")
	result = "%s_%s.%s" %(txt_list1[0], txt_list[0], txt_list1[1])
	print result
	a.append(result+"\n")


fw=open("test.txt","w")
fw.writelines(a)
fw.close
