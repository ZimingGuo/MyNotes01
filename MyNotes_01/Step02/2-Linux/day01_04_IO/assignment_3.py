# author: Ziming Guo
# time: 2020/3/15
'''
作业3：
    编写一个程序，向文件中写入当前时间：
    当 退出程序后 再次执行的时候 会接着上次的编号继续写


   每隔1秒写入一次，每条占一行。
   ctrl-c/红点 结束程序，下次启动后序号要跟之前的连续
   需要可以在编辑器中实时看到文件写入情况
'''
import time

file = open('write_time.txt', 'a+')

file.seek(0, 0)  # 移动到开头
n = 0
for line in file:  # 这个循环的作用就是判断之前写了多少行，以便于之后继续书写
    n += 1

# 开始写入
while True:
    n += 1
    time.sleep(1)
    to_show = "%d.%s\n" % (n, time.ctime())
    file.write(to_show)
    file.flush()  # 作用就是可以随时写进磁盘，方便查看
