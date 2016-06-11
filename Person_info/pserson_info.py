#coding=utf8
#by cw
#by 20160605

Fn_pserson= 'D:\chenwei\python_notes\Person_info\persons.txt'


Person_Direct={}
Fn_read = open(Fn_pserson, 'r')
for line in Fn_read:        #读取文件，生成字典
   Person_Direct[line.split('|')[0]] = line.split('|')

Fn_read.close()
while True:
    Input_info = raw_input('Search info : ')

    m_counter=0
    for key, value in Person_Direct.items():   #读取字典列表
      if key.find(Input_info)!= -1:
          m_counter=m_counter+1
          print value
      else:
        for line in value:                 #查找剩余的值
          if line.find(Input_info)!= -1:   #查找字符串是否匹配，-1表示不匹配
               print value
               m_counter=m_counter+1
    print 'Matched %s' % m_counter
