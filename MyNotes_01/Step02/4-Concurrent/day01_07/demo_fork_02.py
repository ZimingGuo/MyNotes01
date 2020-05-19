# author: Ziming Guo
# time: 2020/3/28
'''
    fork 02
'''

import os
from time import sleep

print("============================")
a = 1

# 创建一个子进程
pid = os.fork()

if pid < 0:
    print("creat process failed")

# 子进程部分要执行的内容
elif pid == 0:
    print("New Process")
    print("a=", a)
    a = 10000 # 这里改变的 a 是改变的子进程自己的 a ，和父进程没有关系

# 父进程部分要执行的内容
else:
    sleep(1)
    print("Old Process")
    print("a:", a) # 打印的还是a=1，因为父进程不会执行 elif 那一部分

# 父子进程共同执行的部分
print("Fork test over")
