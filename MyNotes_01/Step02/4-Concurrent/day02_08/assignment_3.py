# author: Ziming Guo
# time: 2020/3/30
'''
    作业3：
    创建两个进程，分别复制一个文件的上半部分和下本部分，将复制之后的内容放到两个新的文件中
    * 上下部分 同时复制
    * 可能是文本 可能是二进制文件
    * 按照字节的数量分文件的上下部分
'''

import multiprocessing as mp

file01 = open('test_file.txt', 'rb+')
file02 = file01.read()


def divide01():
    file04 = open('assign_upper_file.txt', 'wb+')
    file04.write(file02[0:(len(file02) // 2)])
    print("上层结束")


p = mp.Process(target=divide01)
p.start() # 开启子进程-复制上半部分

# 父进程-复制下半部分
file05 = open('assign_down_file.txt', 'wb+')
st = len(file02) // 2
end = len(file02)
file05.write(file02[st:end])
print("下层结束")

p.join()
