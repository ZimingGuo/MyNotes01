# author: Ziming Guo
# time: 2020/3/27
'''
    demo_fork:
'''

import os
from time import sleep

# 创建一个子进程
pid = os.fork()

if pid < 0:
    print("creat process failed")

# 子进程部分要执行的内容
elif pid == 0:
    sleep(3)
    print("New Process")

# 父进程部分要执行的内容
else:
    sleep(4)
    print("Old Process")

#父子进程共同执行的部分
print("Fork test over")
