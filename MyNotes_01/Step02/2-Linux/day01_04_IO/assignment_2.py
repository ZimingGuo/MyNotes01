# author: Ziming Guo
# time: 2020/3/15
'''
    作业2：
    编写一个文件的拷贝程序：
        从终端输入一个文件
        将文件保存在当前的目录下
        思路：先打开一个文件；然后读出来；在当前目录下写进去
'''
filename = input("输入一个文件名:")
try:
    file01 = open(filename, 'rb')  # 万全之策就是用二进制的读写方式，可以应对任何格式文件
except FileNotFoundError as e:
    print(e)
else:
    file02 = open('Copy_file', 'wb')
    target01 = file01.read(8)
    while target01:
        file02.write(target01)
        target01 = file01.read(8)

    file01.close()
    file02.close() # 之后一定记得关闭文件
