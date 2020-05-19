# author: Ziming Guo
# time: 2020/3/28
'''
    demo
    用信号的方式处理僵尸进程(第三种方法)
'''

import os, sys
import signal

# 表示子进程退出时，父进程忽略退出行为，此时子进程由系统处理
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    print("Child PID", os.getpid())
    sys.exit("Process has exited.")
else:
    while True:  # 这个死循环就是为了不让父进程推出，以为一旦父进程退出，操作系统就会自动处理僵尸进程
        pass
