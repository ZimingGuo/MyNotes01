# author: Ziming Guo
# time: 2020/4/18
'''
    练习：将单词本存入数据库
        创建数据库 & 表的语句 create table words(id int primary key auto_increment,word char(32),mean text);
        1）创建数据库 dict（utf8）
        2）创建数据表 words 将单词和单词解释存入不同的字段
        3）编写程序 将单词存入 words 单词表 超过19500条即可
    思路：
        读一行，当遇到空格的时候就表示这个单词结束了
'''

import pymysql

file01 = open('dict.txt', 'rb+')

# 创建数据库连接
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='19971023gzm',
                     database='dict',
                     charset='utf8')

# 创建游标
cur = db.cursor()

while True:
    # 输入单词
    voca = file01.readline()
    data01 = voca[0:15]
    if not data01:
        break
    data02 = voca[16:len(voca)]

    try:
        sql = "insert into my_words (word,meaning) values(%s,%s);"
        cur.execute(sql, [data01, data02])
        db.commit()

    except Exception as e:
        db.rollback()
        print(e)

# 关闭二者
cur.close()
db.close()
file01.close()
