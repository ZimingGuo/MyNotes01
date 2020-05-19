# author: Ziming Guo
# time: 2020/4/19
'''
    demo04:
    二进制文件的存储演示
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

# # 对二进制文件的存储（图片）
# with open('111.png', 'rb') as file01:
#     data = file01.read()  # 读取出来的date自然就是一个字节串的格式
# try:
#     sql = "update class set image=%s where name='Abby';"
#     cur.execute(sql, [data])  # 这个地方后面的[]是不可以传递表名的，只可以传递
#     db.commit()
# except Exception as e:
#     db.rollback()
#     print(e)

# 把图片提取出来，然后再写入
sql = "select image from class where name='Abby';"
cur.execute(sql)
data = cur.fetchone()
with open('111_copy.png', 'wb') as file02:
    file02.write(data[0])

# 关闭游标 & 数据库
cur.close()
db.close()
