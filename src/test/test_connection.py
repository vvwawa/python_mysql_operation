'''
Created on 2018年2月24日

@author: Administrator
'''
import pymysql

conn = pymysql.Connect(
                       host = 'localhost', #本地mysql地址
                       port = 3306,  #端口
                       user = 'root',   #用户名
                       passwd = 'root', #密码
                       db = 'test',   #数据库
                       charset = 'utf8' #字符
                       )

cursor = conn.cursor()   #获取游标对象

print(conn)
print(cursor)

cursor.close()
conn.close()