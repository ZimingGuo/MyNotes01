# author: Ziming Guo
# time: 2020/3/31
'''
    练习1：
'''

from threading import Thread
from time import sleep, ctime


class MyThread(Thread):
    def __init__(self, target=None, args=(), kwargs={}):
        self.target = target
        self.args = args
        self.kwargs = kwargs
        # 把这几个变成了属性

        super().__init__()  # 此行不允许传参

    def run(self):
        self.target(*self.args, **self.kwargs)


###################################################

def player(sec, song):
    for i in range(3):
        print("Playing %s : %s" % (song, ctime()))
        sleep(sec)


t = MyThread(target=player, args=(3,), kwargs={'song': 'hahaha'})  # 这句话相当于是在使用自己创建的类来实现一个线程
# 上面的这个对象里的参数，是要传给 init 的
# 然后 init 又把这些变量的赋值传给了自己里面的 self.xxx ，也就相当于是传给了自己，以备后用(之后的 run 会用到)

t.start()
t.join()
