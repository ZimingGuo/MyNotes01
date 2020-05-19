# author: Ziming Guo
# time: 2020/4/1
'''
    作业3的老师版本
    创建两个进程，分别复制文件的上半部分和下半部分
'''

from multiprocessing import Process
import os

filename = 'test_file.txt'
size = os.path.getsize(filename)  # 这句话就是用来获取文件的大小的，超实用
# 父进程创建 fr，两个子进程使用这个相同的 fr 会相互影响

# 复制上半部分
def top():
    fr = open(filename, 'rb')
    fw = open('top.txt', 'wb')
    n = size // 2
    fw.write(fr.read(n))
    fr.close()
    fw.close()


# 复制下半部分
def bot():
    fr = open(filename, 'rb')
    fw = open('bot.txt', 'wb')
    fr.seek(size // 2, 0)
    # 很重要：改变目前的文件偏移量，要从上次结束的地方开始
    # 以开头为基准，向后移动 size//2 个字节
    fw.write(fr.read())  # 啥也不写，默认直接读到最后
    fr.close()
    fw.close()


p01 = Process(target=top)
p02 = Process(target=bot)
p01.start()
p02.start()
p01.join()
p02.join()
