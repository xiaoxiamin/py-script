#!/usr/bin/env python
import string
import random
allchs = string.letters + string.digits
def genPwd(num = 8):
    pwd = ''
    for i in range(num):
        pwd += random.choice(allchs)
    return pwd
if __name__ == '__main__':
    print genPwd()
    print genPwd(6)
