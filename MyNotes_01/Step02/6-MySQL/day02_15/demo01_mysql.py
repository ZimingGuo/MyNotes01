# author: Ziming Guo
# time: 2020/4/18
'''
    demo01:
    pysql操作的基本流程演示
'''

# 导入
import pymysql

# 连接数据库
# db 代表的就是这个 stu 数据库了
db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='19971023gzm',
    database='stu',
    charset='utf8'
)

# 获取游标（用来后续操作数据库，执行 SQL 语句，并且会承载数据结果）
cur = db.cursor()

# 执行 SQL 语句
sql = "insert into class values (8,'ASD',17,'w',78.9,'2020-8-8');"  # 分号可以写可以不写

# 执行语句
cur.execute(sql)

# 写操作需要提交操作
# 可以先执行多个写操作，然后一起提交
# 只有有了这个 commit 的语句之后，数据库才会根据 execute 的语句进行更改，不然不会改变的
db.commit()

# 关闭游标，意味着之后游标失效
cur.close()

# 关闭数据
db.close()
