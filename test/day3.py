#coding=utf8

age = 100

def Hellowork(name):
    global age
    age = 50
    '''this is hello work!'''
    print 'Hello,%s, old!!' % age


Hellowork('Chen wei!!!')

print 'age:',age

#map


#pickle

import pickle

account_info={
    '123':['cw',11,22],
    '1234':['ww',24,22]

}

f=file('tmp.txt','wb')

pickle.dump(account_info,f)
f.close()

