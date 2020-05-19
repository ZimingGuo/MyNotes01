# author: Ziming Guo
# time: 2020/3/28
'''
    demo 模拟僵尸进程的产生
'''

import os, sys

pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    print("Child PID", os.getpid())
    sys.exit("Process has exited.")
else:
    '''
    os.wait()处理僵尸进程
    '''
    pid, status = os.wait()
    print("pid:", pid)
    print("status:", status) # 相当于是子进程的退出状态 * 256

    while True:  # 这个死循环就是为了不让父进程推出，以为一旦父进程退出，操作系统就会自动处理僵尸进程
        pass
