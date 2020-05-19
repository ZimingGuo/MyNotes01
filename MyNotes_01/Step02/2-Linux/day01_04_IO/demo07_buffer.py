# author: Ziming Guo
# time: 2020/3/16
"""
    demo07：
        buffer.py
        缓冲区刷新测试
缓冲区刷新条件：
1）缓冲区满了
2）行缓冲在换行时会自动刷新
3）程序运行结束 or 文件close关闭
4）调用flush()函数
"""

# f = open('a.py','w',1) # 行缓冲，当调用行缓冲的时候，只有遇到了换行符号才会把缓冲区数据写入磁盘
f = open('test.txt', 'w')

while True:
    data = input(">>")
    if not data:
        break
    f.write(data + '\n')
    f.flush()  # 刷新缓冲区

f.close()
