#!/bin/python
# -*- coding=UTF-8 -*-

import re

log_file=raw_input(please input log file:)
log=open('log_file')
all_log=log.read()
log.close()

search_user=raw_input("please input your search user:")

#search_log=re.compile('Connect([\s\S]*)Connect')
#input_log=search_log.findall(all_log)
#print input_log

lst=all_log.split("Connect")
for i in lst:
        if search_user in i:
                print i
