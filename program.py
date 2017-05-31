#!/usr/bin/python
import os

while True:
	input = raw_input("Please input your username:")
	if input == 'simin':
		password = raw_input("Please input your password:")
		p = 'simin'
		while password != p:
			password = raw_input("Wrong passwd,input again:")
		else: 
			print "Welcome Login to program!"
			while True:
				match = "NO"
				input = raw_input("Please input the name whom you want to search:")
				contack_list = file('contack_list')
				while True:
					line = contack_list.readline()
					if len(line) == 0:break
					if input !="" and input in line:
						print "Match item : %s" %line
						match = "YES"
					else:
						pass
				if match != "YES": print "no match item!"
	else:
		print "sorry username not found!"
