#!/bin/bash
#!coding=utf8

#by author cw
#2016-06-05


#定义产品线,有新产品，可以再这里添加
products=[
    ['Meizu Mx5',2000],
    ['Ipad air 2',3000],
    ['Dell notebook',10000],
    ['Coffee',50],
    ['Book',100]
]

#处理产品菜单列表
def Menu_Cart():
    i = 0
    for pp in products:
        i = i + 1
        print "%s. %s" % (i, pp)

#输入检查
def Input_Check(Input):
    if len(Input) == 0:
        print "Your input is not correct."
        return False

def Go_Buy(salary,Num):   #添加到购物车，扣工资
    if int(salary) >= products[Num][1]:
        #print products[Num][1]
        salary = int(salary) - products[Num][1]
        print "Your salary is %s " % salary
    else:
        print "Your salary not enougth,please select other product!"
        print "Your salary is %s " % salary
    return salary


User_Salary=raw_input('Please input your salary ：\t')
if Input_Check(User_Salary) == False:
    exit()

while True:
    min_s = int(User_Salary)        #定义所有产品最小值
    #print "min salary %s" % min_s
    for Product_price in products:
        if min_s > Product_price[1]:
                min_s = Product_price[1]
    if int(User_Salary) <= int(min_s):
        print "Your cannot afroid anything,Please continue Work Hard!"
        exit()
    else:
        Menu_Cart()
        Shop_Select=raw_input('Please want to input products Number : \t')
        if Input_Check(Shop_Select) == False:
            print "Your salary is %s " % User_Salary
            continue
        Shop_Select=int(Shop_Select)
        if Shop_Select == 1:
            User_Salary=Go_Buy(User_Salary,0)
        elif Shop_Select == 2:
            User_Salary = Go_Buy(User_Salary, 1)
        elif Shop_Select == 3:
            User_Salary = Go_Buy(User_Salary, 2)
        elif Shop_Select == 4:
            User_Salary = Go_Buy(User_Salary, 3)
        elif Shop_Select == 5:
            User_Salary = Go_Buy(User_Salary, 4)
        else:
            print "Error"
Menu_Cart()

