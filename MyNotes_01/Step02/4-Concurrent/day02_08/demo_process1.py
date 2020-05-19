# author: Ziming Guo
# time: 2020/3/29
'''
    multiprocessing 模块创建进程
    1）编写进程对象
    2）生成进程对象
    3）启动进程
    4）回收进程
'''

import multiprocessing as mp
from time import sleep
import os

a = 1


# 编写进程函数
def fun01():
    print("开始一个进程")
    sleep(5)
    global a
    print('a = ', a)
    a = 10000 # 这个修改的 10000 只是在子进程里有效，而子进程只执行这一个函数，其他都是父进程执行
    print("子进程结束")


# 创建进程对象
p = mp.Process(target=fun01)
# 通过 Process 类创建进程对象，绑定函数，target 是目标函数
# p 就是创建出来的一个对象，multiprocessing 是一个类
# 下载 p 就可以代表这个进程了，只是代表，不是真是

p.start()  # 启动子进程，也就是通过类调用方法的形式

# 父进程事件，只能写在 start & join 这两句话之间，这才表示二者同是进行
sleep(2)
print("父进程事件")

p.join()  # 阻塞等待子进程结束，回收子进程，通过类调用方法（回收可以有效阻止僵尸进程的产生）
# 注意：想要在 join 之后干点事，都要等到子进程结束才能做，因为 join 是阻塞函数
# 如果不加这个 join 子进程结束后，父进程还没有结束，就会变成僵尸进程

print('a:', a) # 打印出来还是 1 ，父进程不会执行子进程的部分，不会修改

# 上面的三行代码，等同于：
'''
pid = os.fork()
if pid == 0:
    fun01()
    os._exit()
else:
    os.wait()
'''
# 在开辟空间上，上面两种方式也是一样的

# 经验：
# 如果想要执行很多个进程，一般不进程啥也不干，会把所有的进程都分给子进程

# fork 不适合做对进程，两个是适合的
