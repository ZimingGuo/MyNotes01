# author: Ziming Guo
# time: 2020/4/18
'''
    demo03:
    pymysql写操作示例（insert update delete 增删改）
'''
# 一般的步骤就是：创建数据库连接 & 生成游标 & 关闭数据库和游标
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

# 写数据库
# 加上 try 之后就可以防止错误执行了
try:
    # 写 sql 语句执行
    # 插入操作
    # name = input('Name:')
    # age = input('Age:')
    # score = input('Score:')

    # 写操作
    # sql = "insert into class (name,age,score) values ('%s',%d,%f);" % (name, int(age), float(score))
    # # 一定要注意，字符串两侧加引号！
    # cur.execute(sql) # 执行

    # 写操作（用 execute列表传参的方式）
    # sql = "insert into class (name,age,score) values (%s,%s,%s);"
    # cur.execute(sql,[name,age,score]) # 这个列表的参数就是起到了自动传递进去，此时字符串的外层引号不用加了
    # db.commit() # 提交

    # 修改操作
    # sql = "update interest set price=12000 where name='Bob'"
    # cur.execute(sql)
    # db.commit()

    # 删除操作
    sql="delete from class where score<80;"
    cur.execute(sql)
    db.commit()

except Exception as e:
    db.rollback()  # 退回到 commit 执行之前的数据库状态，不会破坏数据库
    print(e)

# 关闭游标
cur.close()

# 关闭数据库
db.close()
