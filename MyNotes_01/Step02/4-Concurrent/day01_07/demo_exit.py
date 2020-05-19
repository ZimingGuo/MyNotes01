# author: Ziming Guo
# time: 2020/3/28
'''
    demo 退出进程
'''
import os, sys

# 有一点很重要，父子进程的结束对对方都没有影响
# 结束自己的进程，对方都会继续运行

# os._exit(0)
sys.exit("Process has been exited")

print("print something")
