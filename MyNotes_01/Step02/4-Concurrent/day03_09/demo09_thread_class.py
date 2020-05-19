# author: Ziming Guo
# time: 2020/3/31
'''
    dmeo_thread_class
    自定义线程类
'''

from threading import Thread


# 自定义线程类
class ThreadClass(Thread):  # 表示自己创建一个类，叫做 ThreadClass

    # 自己写一个 init，但是相当于重写了父类的 init(写完这些就代表既有了原来父类的属性，又有了新的自己写的属性)
    def __init__(self, *args, **kwargs):
        self.attr = args[0]

        # 这句话是必须的，因为需要父类中的一些属性，没有父类属性，之后就没法操作了
        super().__init__()  # 这句话表示 加载父类 init 的属性

    # run 起到了类里面功能启动的作用
    # 假设需要很多步骤完成
    # 根据实际需要来写
    def fun01(self):
        print("step1")

    def fun02(self):
        print("step2")

    # 重写run 逻辑调用
    # 在之前，上面的部分，我想写啥函数就写啥函数，只要在最后用 run 作为一个逻辑调用函数就可以了
    def run(self):
        # 在类外，直接 start 的时候，就可以先直接调用 run，然后就会启动里面的 fun01 和 fun02
        self.fun01()
        self.fun02()


t = ThreadClass('abc')
t.start()  # 在我们之前创建类的时候，我们并没有写 start，所以这个start的方法是继承过来的
t.join()  # join 也同上


# 综上，可以发现，我调用这个新建的类，实际上是可以完成一个比较复杂的线程的