#coding=utf8

print '测试'


class Person:
    def __init__(self,name,age):
        print 'I am being called right now ....'
        self.Name = name
        self.Age = age
    def sayHi(self):
        print 'hi name %s,old %s' %(self.Name,self.Age)
        self.__talk()
    def __talk(self):
        print 'I am private.....'


p= Person('chenwei',20)
p.sayHi()


#######-----------####################

class SchoolMember:
    def __init__(self,name,gender,nationality='CN'):
        self.name=name
        self.gender = gender
        self.nation = nationality

    def tell(self):
        print 'Hi,my name is %s,I am from %s' %(self.name,self.nation)

class Student(SchoolMember):
    def __init__(self,Name,Gender,Nation,Class,Score):
        SchoolMember.__init__(self,Name,Gender,Nation)  #继承基础类变量
        self.Class = Class
        self.Score = Score

    def payTuition(self,amount):
        if amount < 6499:
            print 'Get the fuck off....'
        else:
            print 'Welcome onboard!'

class Teacher(SchoolMember):
    def __init__(self,Name,Gender,Course,Salary,Nation):
        SchoolMember.__init__(self,Name,Gender,Nation)
        self.Course = Course
        self.Salary = Salary

    def teachering(self):
        print 'I am teaching %s,i am making %s per month ！' % (self.Course,self.Salary)


S1 = Student('chenwei','Male','python','c+',90)
S1.tell()
S1.payTuition(4999)

S2 = Student('Shit','Male','pythonaaa','B','B+')
S2.tell()

T1 = Teacher('cw','male','java','c++',500)
T1.tell()
T1.teachering()

import time
print time.localtime()