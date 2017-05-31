#!/usr/bin/python
#-*- coding=UTF-8 -*-

import web
import commands

urls=(
"/(.*)","Index"
)

class Index:
        def GET(self,arg):
                	if arg=="deploy=yes":
                        	a , b = commands.getstatusoutput("/bin/bash /home/xiamin/simin.sh")
				if a == 0 :
					return "it's ok "
				else:
					return "it's false : %s" %b
app=web.application(urls,globals())
if __name__ == "__main__":
	app.run()
