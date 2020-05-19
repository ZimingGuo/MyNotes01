# author: Ziming Guo
# time: 2020/4/18
'''
    demo02:
    pymysql 读操作示例（其实就是SQL中的select）
'''

import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='19971023gzm',
                     database='stu',
                     charset='utf8')

# 获取游标（操作数据库，执行sql语句）
cur = db.cursor()

# 获取数据库数据
sql = "select * from class where gender='m';"
cur.execute(sql)  # 语句执行正确之后，cur再调用函数，获取结果，而不是直接返回结果

# # 获取一个查询结果
# one_row = cur.fetchone()  # 这个获取到的结果是一个元组，多元素元组
# print(one_row)

# # 获取多个查询结果
# many_row = cur.fetchmany(2) # 获取两个查询结果，元组里面有两个元组
# # 获取的这两个结果是接着上次查找的地方开始的
# print(many_row)

# 获取所有查询结果
all_row = cur.fetchall()
print(all_row)

# 关闭游标
cur.close()

# 关闭数据库
db.close()
