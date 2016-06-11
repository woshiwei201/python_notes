#coding=utf8
# main atm
#by cw
#2016-06-06

import pickle
import time
Person_conf='D:\chenwei\python_notes/atm/Person_Cart.dat'
Person_Cart='D:\chenwei\python_notes/atm/Person_Cart_tmp1.dat'
Record_log_File='D:\chenwei\python_notes/atm/record_log_file.dat'
#定义用户字典
Dict_Person={}

def User_Login_Check(username,passwd):  #如何判断用户名
    Flag=False
    (u, p, c, b) = Read_Person_Pick(Person_Cart, username)  # 返回用户名，密码，信用额度，剩余额度
    if len(username) == 0 or len(passwd) == 0:
        print "The Username or Password cannot null!"
    elif str(u)==username and str(p) == passwd:
        Flag=True
    else:
        print "Error"

    return Flag



def User_Login_Fun(username,passwd,shop_price,shop,type):

    (u,p,c,b)=Read_Person_Pick(Person_Cart,username)  #返回用户名，密码，信用额度，剩余额度
    if type == "cachin":  #存款
            c = int(c) + int(shop_price)
            Modify_Person_Pick(Person_Cart, username, c, b)
            Logging_Record(username, Date_Y, type, str('-')+str(shop_price), 0)
    elif type == "gotoshop":  #g购物
        if int(c) < int(shop_price):
            print "Your cannot payment %s ,your balance only %s " % (shop_price,b)
        else:
           b=int(b)-int(shop_price)
           Modify_Person_Pick(Person_Cart,username,c,b)
           Logging_Record(username, Date_Y,shop,shop_price,0)
    elif type == "takecash":  #取款
        c = c - int(shop_price)
        interest = int(shop_price) * 0.0005
        Modify_Person_Pick(Person_Cart, username, c, b)
        Logging_Record(username, Date_Y, type, c, interest)



def Logging_Record(username,tran_date,type,apay,interest):
    Fn=file(Record_log_File,'a')
    msg="%s %s  %s  %s  %s "  % (tran_date,username,type,apay,interest)
    Fn.write(str(msg)+'\n')
    Fn.close()

def Buy_Shop():
    pass


def Modify_Person_Pick(file, user, creadit_tm, balance_t):   #修改信用额度等信息
    fn = open(file, 'rb')
    Dict_Pick_t = pickle.load(fn)
    #   for line in Dict_Pick_t:

    #      if line == str(user):
    #         print Dict_Pick_t[line]   #打印字典信息
    fn.close()
    fn = open(file, 'wb')
    for line in Dict_Pick_t:
        # print line
        if line == str(user):
            print Dict_Pick_t[line]  # 打印字典信息
            Dict_Pick_t[line][2] = creadit_tm  # creadit
            Dict_Pick_t[line][3] = balance_t  # balance

            print 'The modify : %s ' % Dict_Pick_t[line]  # 打印字典信息
    pickle.dump(Dict_Pick_t, fn)
    fn.close()


def Read_Person_Pick(file, user):     #序列化读取配置文件，获取 用户，密码，信用额度，balance等信息
    fn = open(file, 'rb')
    Dict_Pick_r = pickle.load(fn)
    for line in Dict_Pick_r:
        if line == str(user):
            return Dict_Pick_r[line]  # 打印字典信息
    fn.close()
    return False   #没有查询到用户信息

## ATM
Date_t=time.localtime()
Date_Y=str(Date_t[0])+"/"+str(Date_t[1])+"/"+str(Date_t[2])

Fn = open(Person_Cart)
for line in Fn.readlines():
    Dict_Person[line.split('|')[0]] = line.split('|')




#print Dict_Person
while True:

   print '''
    1. Go go Shopping!
    2. To ATM deposit.
    3. To ATM Take cash.
    4. Check the bill.
    5. init main.
    6. Exit.
    '''
   Select_ATM_Num=raw_input('Please input number : ')
   if  len(Select_ATM_Num) == 0:
        print "Error,please input number right."
        continue
   else:
        if int(Select_ATM_Num) == 1:     #选择去商店购物
           print "111"
           while True:
                 print '''
                 1.Coffee shop  48
                 2.Shoes shop  500
                 3.book shoop  300
                 4.Go to ATM menu.
                '''
                 Select_Buy_Num = raw_input('Please input number : ')
                 if  len(Select_Buy_Num) == 0:
                     print "Error,please input number right."
                     continue
                 else:
                     if int(Select_Buy_Num) == 1:
                         Username = raw_input('Please input your Username: ')
                         Password = raw_input('Please input your Password: ')
                         if User_Login_Check(Username,Password) == False:
                             print "The Username or Password is error!please input again!"
                             continue
                         else:
                            User_Login_Fun(Username, Password, 48, 'Coffee shop', 'gotoshop')
                            print "Welcome"



                     if int(Select_Buy_Num) == 2:
                         Username = raw_input('Please input your Username: ')
                         Password = raw_input('Please input your Password: ')
                         if User_Login_Check(Username, Password) == False:
                             print "The Username or Password is error!please input again!"
                             continue
                         else:
                             User_Login_Fun(Username, Password, 500, 'Shoes shop', 'gotoshop')
                             print "Welcome"
                     if int(Select_Buy_Num) == 3:
                         Username = raw_input('Please input your Username: ')
                         Password = raw_input('Please input your Password: ')
                         if User_Login_Check(Username, Password) == False:
                             print "The Username or Password is error!please input again!"
                             continue
                         else:
                             User_Login_Fun(Username, Password, 300, 'book shoop', 'gotoshop')
                             print "Welcome"
                     if int(Select_Buy_Num) == 4:
                         break
        if int(Select_ATM_Num)  == 2:
            print "To ATM deposit"
            Username = raw_input('Please input your Username: ')
            Password = raw_input('Please input your Password: ')
            Price = raw_input('Please input Cashin numbers :')
            if User_Login_Check(Username, Password) == False:
                print "The Username or Password is error!please input again!"
                continue
            else:
                User_Login_Fun(Username, Password, Price, 'Coffee shop', 'cachin')
                print "Welcome"


        if int(Select_ATM_Num)  == 3:
            print "To ATM Take cash"
            Username = raw_input('Please input your Username: ')
            Password = raw_input('Please input your Password: ')
            Price = raw_input('Please input Take cash numbers :')
            if User_Login_Check(Username, Password) == False:
                print "The Username or Password is error!please input again!"
                continue
            else:
                User_Login_Fun(Username, Password, Price, 'Coffee shop', 'takecash')
                print "Cash in Susses!"


        if int(Select_ATM_Num) == 4:
            print "your input 4"

        if int(Select_ATM_Num) == 5:
            print "init conf"
            Dict={}
            fn=open(Person_conf,'rb')
            fn2=open(Person_Cart,'wb')
            for line in fn.readlines():
                 if line.split('|')[0]  != 'Account':
                   Dict[line.split('|')[0]] = [line.split('|')[0].strip(),line.split('|')[1].strip(),line.split('|')[2].strip(),line.split('|')[3].strip()]
            print Dict

            print "ppick"
            pickle.dump(Dict,fn2,True)
            fn.close()
            fn2.close()


        if int(Select_ATM_Num) == 6:
            print "Exit"
            exit()



