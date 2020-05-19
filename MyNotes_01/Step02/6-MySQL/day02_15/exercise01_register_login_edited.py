# author: Ziming Guo
# time: 2020/4/19
'''
    模拟注册登录
'''

import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='19971023gzm',
                     database='stu',
                     charset='utf8'
                     )

# 创建游标
cur = db.cursor()


def register():
    name = input("用户名:")
    password = input("密码:")
    sql = "select * from user where name='%s'" % name
    cur.execute(sql)
    result = cur.fetchone()  # 如果没有这个用户名的话就返回空
    if result:
        return False
    try:
        sql = "insert into user (name,passwd) values (%s,%s);"
        cur.execute(sql, [name, password])
        db.commit()
        return True
    except:
        db.rollback()
        return False


def login():
    name = input("用户名:")
    password = input("密码:")
    sql = "select * from user where name='%s' and passwd='%s'"
    cur.execute(sql)
    result = cur.fetchone()
    if result:
        return True


while True:
    print("1-注册 or 2-登录")
    cmd = input("输入命令:")
    if cmd == '1':
        # 执行注册
        if register():
            print("注册成功！")
        else:
            print("注册失败！")
    elif cmd == '2':
        # 执行登录
        if login():
            print("登录成功！")
            break
        else:
            print("登录失败！")
    else:
        print("无此功能")

# 关闭
cur.close()
db.close()
