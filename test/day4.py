#coding=utf8
f='D:\chenwei\python_notes/test\Person_Cart.dat'
f1='D:\chenwei\python_notes/test\Person_Cart_tmp.dat'
import pickle
Dict={}
# fn=open(f,'rb')
# fn2=open(f1,'wb')
# for line in fn.readlines():
#      Dict[line.split('|')[0]] = line.split('|')
# print Dict
#
# print "ppick"
#
# pickle.dump(Dict,fn2,True)
# fn.close()
# fn2.close()
#
#


# ####read#############
#
#
# fn2=open(f1,'rb')
# a = pickle.load(fn2)
#
# print "-------"
# fn2.close()
# print a
#
# fn2=open(f1,'wb')
#
#
# for line in a:
#    print line,a[line]
#    if line == '99999999':
#       print line,a[line]
#    for list in a[line]:
#      print list
#
#
#
# pickle.dump(a,fn2)
# print "aaaaaa"
# print a
# fn2.close()
# ####



def Modify_Person_Pick(file,user,creadit_tm,balance_t):
      fn=open(file,'rb')
      Dict_Pick_t=pickle.load(fn)
   #   for line in Dict_Pick_t:

   #      if line == str(user):
   #         print Dict_Pick_t[line]   #打印字典信息

      fn.close()

      fn = open(file, 'wb')

      for line in Dict_Pick_t:
         # print line
         if line == str(user):
            print Dict_Pick_t[line]  # 打印字典信息
            Dict_Pick_t[line][2] = creadit_tm      #creadit
            Dict_Pick_t[line][3] = balance_t     #balance
            print 'The modify : %s ' % Dict_Pick_t[line]  # 打印字典信息
      pickle.dump(Dict_Pick_t,fn)
      fn.close()

def Read_Person_Pick(file, user):
          fn = open(file, 'rb')
          Dict_Pick_r = pickle.load(fn)
          for line in Dict_Pick_r:
                if line == str(user):
                   return Dict_Pick_r[line]   #打印字典信息
          fn.close()

(u,p,c,b)= Read_Person_Pick(f1,88888888)
print u
print p
print c
print b

#Modify_Person_Pick(f1,99999999,88881,999991)


import time

Date_t=time.localtime()
Date_Y=str(Date_t[0])+"/"+str(Date_t[1])+"/"+str(Date_t[2])
#print "%s\/%s\/%s " % (Date_t(0),Date_t(1),Date_t(2))