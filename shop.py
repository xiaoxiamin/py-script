#!/bin/python
#-*- coding:UTF-8 -*-

#import /etc/python/pystartup

f=file('shop_list')

products=[]
prices=[]
shop_list=[]

for line in f.readlines():
	new_line=line.split()
	products.append(new_line[0])
	prices.append(int(new_line[1]))

salary = int(raw_input('Please input your salary:'))
while True:
	print "Welcome,things you can but as below:"
	for p in products:
		p_index = products.index(p)
		p_prices = prices[p_index]
		print p,p_prices
	choice=raw_input('Please input what you want to buy:')
	if choice in products:
		print "\033[31mYes,it is in the list.\033[0m"
		p_index = products.index(choice)
		p_prices=prices[p_index]
		print '\033[31m %s,%s\033[0m'%(choice,p_prices)
		if salary >= p_prices:
			print "Congratulations added %s to shop list"
			shop_list.append(choice)
			salary -= p_prices
			if salary < min(prices):
				print ""
			else: print
		else:
			print ""
	else: print "\033[31mSorry,it's not on the list\033[0m"
	
	
