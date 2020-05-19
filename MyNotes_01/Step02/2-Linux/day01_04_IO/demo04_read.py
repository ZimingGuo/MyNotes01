# author: Ziming Guo
# time: 2020/3/15
"""
file_read.py
文件读取演示
"""

# 打开文件
f = open('Install.txt', 'r')

# 读取文件
# data = f.read()
# print(data)

# 循环读取文件内容
# while True:
#     # 如果读到文件结尾 read()会读到空字符串
#     data = f.read(1024)
#     # 读到结尾跳出循环
#     if not data: # 读到最后，data就是空了，非空就break
#         break
#     print(data)

# 读取文件一行内容
# data = f.readline(5) # 读取第一行五个字
# print(data)
# data = f.readline(5) # 再调用，读取第一行接下来五个字
# print(data)

# 读取内容形成列表
# data = f.readlines(20)  # 读取前20个字节所在的所有行
# print(data)

# 使用for循环读取每一行
for line in f:
    print(line)  # 每次迭代到一行内容

# 关闭
f.close()
