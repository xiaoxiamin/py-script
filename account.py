#!/bin/python

import pickle

account_info = {'1111111':['simin',15000,15000],
		'2222222':['oldboy',15000,15000],
		}

f = file('account.pkl','wb')

pickle.dump(account_info,f)

f.close()
