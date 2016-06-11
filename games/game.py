#coding=utf8
#by cw
# 游戏人生

class Person:
    assets = 0
    school_name = None
    Interview = ['360','Baidu','Ali','Tengxun']
    attraction = 0
    skills = []
    love_status = None
    lover = None
    job = None
    company = None

    def __init__(self,name,sex,role):
        self.name = name
        self.sex = sex
        self.role = role
        print '\033[32;1m-\033[0m'*60
        if self.role == 'rich':
            self.assets += 10000000
            self.attraction +=80
            print '\033[32;1m My name is %s,I am a %s guy,I have %s money! It is good to be rich... \033[0m'\
            % (self.name,self.role,self.assets)
        elif self.role == 'poor':
            self.assets += 5000
            self.attraction +=40
            print '\033[31;1m My name is %s,I am a %s guy,I have %s money! I hate to be pool,but .. life is fucking hard.. \033[m' %\
          (self.name,self.role,self.assets)
        elif self.role == 'beauty':
            self.assets +=5000
            self.attraction +=90
            print '\033[32;1m My name is %s , I am a %s girl,I do not have much money,\
          but I am very beautiful,that makes me feel good and confident,but I do \
          not want to be poor forever. \033[0m' %(self.name,self.role)

    def talk(self,msg,tone='normal'):
        if tone == 'normal':
            print '\033[32;1m %s: %s \033[0m' % (self.name,msg)
        elif tone == 'angry':
            print '\033[31;1m%s : %s\033[0m'  % (self.name,msg)

    def assets_balance(self,amount,action):
        if action == 'earn':
            self.assets += amount
            print '\033[32;1m %s  just made %s RMB! Current assets is %s \033[0m' %(self.name,amount,self.assets)
        elif action == 'cost':
            self.assets -= amount
            print '\033[32;1m%s just made %s RMB! Current assets is %s \033[0m' %(self.name,amount,self.assets)

p1 = Person('CW','male','poor')
p1.talk('Hello,my guys!')
p1.assets_balance(300,'earn')