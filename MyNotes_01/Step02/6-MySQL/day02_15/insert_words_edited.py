# author: Ziming Guo
# time: 2020/4/18
'''
    上一个练习的修订版本：
        将单词本存入数据库
        创建数据库 & 表的语句 create table words(id int primary key auto_increment,word char(32),mean text);
        1）创建数据库 dict（utf8）
        2）创建数据表 words 将单词和单词解释存入不同的字段
        3）编写程序 将单词存入 words 单词表 超过19500条即可
    思路：
        读一行，当遇到空格的时候就表示这个单词结束了
'''

import pymysql
import re  # 一会要用到正则表达式的方法匹配 word 和 mean ，所以导入 re

file01 = open('dict.txt', 'r')

# 创建数据库连接
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='19971023gzm',
                     database='dict',
                     charset='utf8')

# 创建游标（游标是用来操作数据库的，便于之后执行sql语句）
cur = db.cursor()

# 按照空格分割再拼接去掉空格，这种方式适合用于字符串的提取（一定要熟练 join 和 strip 函数的使用）
# data = file01.readline()
# list_word = data.split(' ')
# word = list_word[0]
# mean = ' '.join(list_word[1:]).strip()  # 从第一个元素往后，按照空格再全都拼接起来，并且去掉两侧的空格
# print(word)
# print(mean)

# 使用正则表达式的方法
sql = "insert into words (word,mean) values (%s,%s);"

for line in file01:
    # 开始获取单词 & 解释
    # 下面这句话就是提取特定字符问题的精髓
    tup = re.findall(r"(\S+)\s+(.*)", line)[0]
    # 此时的这个 tup 就是一个个的元组，两个元素，第一个是单词，第二个是解释
    # \S 表示非空字符 \s+表示空字符，即空格，不知道有多少个
    try:
        cur.execute(sql, tup)  # 把 tup 的参数传给 sql 语句
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)

# 关闭二者
cur.close()
db.close()
file01.close()
