# author: Ziming Guo
# time: 2020/3/30
'''
    demo01_pipe:
    利用管道进行通信
    注：
    1）multiprocessing 中管道通信只能用于有亲缘关系的进程中
    2）管道对象在父进程中创建，子进程通过新建进程的时候 copy 来获取管道，子进程不必再单独创建管道
'''

from multiprocessing import Process, Pipe

# 创建管道
fd1, fd2 = Pipe()
# 默认情况下就是双向管带
# 单向管道的话 fd1 只能读，fd2 只能写


def app1():  # 这个函数就相当于子进程1，因为是 multiprocessing 的方法创建进程
    print("启动 app1，请登录")
    print("请求 app2 的授权")
    fd1.send("app1 请求登陆")  # send 就是向管道内写入内容
    data = fd1.recv()
    if data:
        print("登陆成功", data)


def app2():  # 这个函数就相当于子进程2，因为是 multiprocessing 的方法创建进程
    # 如果用 fd1 写入管带内容，那就要用 fd2 来获取写入的内容，一进一出
    data = fd2.recv()  # 同样是一个阻塞函数，阻塞等地啊读取管道内容
    print(data)
    fd2.send(('Jacky', 123))  # 可以发送任意 python 类型的数据


p1 = Process(target=app1)
p2 = Process(target=app2)

# 开启两个进程
p1.start()
p2.start()

# 回收两个进程
p1.join()
p2.join()
