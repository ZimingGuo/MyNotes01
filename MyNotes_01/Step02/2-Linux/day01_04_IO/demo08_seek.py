# author: Ziming Guo
# time: 2020/3/16
"""
    demo08：
        seek.py  文件偏移量测试
    1）每次用 open 打开文件的时候文件偏移量都是在开头的
    2）用 a 的方式打开文件的时候文件偏移量在结尾
    3）读写操作共用一个文件偏移
"""

# 以r,w打开文件偏移量在开头，以a打开文件偏移量在结尾
f = open("test.txt", 'rb+')
print(f.tell())

# f.write("Hello world")
#
# print(f.tell())

# 以开头为基准向后移动5个字符
f.seek(1024, 0) # 表示从开头开始向后的1024位置
f.seek(-1, 2)  # 表示从结尾开始向前的一个位置
f.seek(10, 2)  # 表示从结尾开始向后的十个位置
# 注意：向前越界是不可以的，向后越界可以

f.write('你好'.encode())
# data = f.read()
# print(data)

f.close()
