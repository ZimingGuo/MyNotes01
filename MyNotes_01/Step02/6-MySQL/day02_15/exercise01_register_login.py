# author: Ziming Guo
# time: 2020/4/19
'''
    练习01：
    编写一段程序模拟注册和登录的过程
    1）创建一个 user 表，包含用户名和密码字段
    2）在应用程序中模拟注册和登录功能
        注册：输入用户名和密码将用户名存入到数据库（用户名不能重复）
        登录：进行数据库比对，如果有该用户则打印登录成功，否则让重新输入
'''

import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='19971023gzm',
                     database='stu',
                     charset='utf8')

# 获取游标
cur = db.cursor()


def register():
    name = input("请输入要注册的用户名:")
    password = input("请设置密码:")
    try:
        sql = "insert into my_user (name,password) values (%s,%s)"
        cur.execute(sql, [name, password])
        db.commit()
        print("注册成功！")
    except Exception as e:
        db.rollback()
        print(e)
        print("此用户名已存在，请重新注册！")


def logon():
    while True:
        name = input("请输入用户名:")
        password = input("请输入密码:")
        try:
            sql = "select * from my_user where name=%s;"
            cur.execute(sql, [name])
            # 深层次的理解：cur的作用就相当于是一个载体，载着读取出来的数据
            info = cur.fetchone()
            if info[2] == password:
                print("登录成功！")
                break
            else:
                print("输入密码错误，请重新输入密码！")
        except Exception as e:
            print("此用户名未注册，请先注册！")
            return


while True:
    print("1-注册  2-登录")
    todo = input("请选择功能:")

    if todo == "1":
        register()
    elif todo == "2":
        logon()
    else:
        print("无此功能，请重新输入！")

# 关闭
cur.close()
db.close()
