# author: Ziming Guo
# time: 2020/3/9
'''
    练习3：
    定义一个顺序的队列
    因为是运用列表，而且是有进有出，进出不在同一端，所以必然会有内存的移动
        思路 :
            1. 基于列表完成数据存储
            2. 对列表功能进行封装
            3. 列表的头部作为队头,尾部作为队尾
            功能: 入队(enqueue),出队(dequeue),判断队列为空
'''


class QueueError(Exception):
    """
        这个异常的类是继承于 Exception 类的
    """
    pass


class SQueue:
    # 初始化
    def __init__(self):
        self._elements = []

    # 判断队列是否为空
    def is_empty(self):
        return self._elements == []

    # 入队
    def enqueue(self, value):
        """
            把列表尾部定义为队尾
        :param value: 要添加的数据
        """
        self._elements.append(value)

    # 出队
    def dequeue(self):
        if self.is_empty():
            raise QueueError("队列为空")
        return self._elements.pop(0)
        # 注意，此处是pop，而不仅仅是查看
        # 所以不用索引，而是 pop


# something puzzling for a long time：
#     程序中的这三个类方法就是这个封装好的类对外提供的按三个接口
#     一直以来不明白啥是接口，这个就是对外界提供的接口
#     也就是说外界只能通过这三个接口来操作类里面的数据
#     绝对不能直接修改 or 查看 _elements


if __name__ == "__main__":
    sq01 = SQueue()
    # print(sq01.is_empty())
    # sq01.enqueue(1)
    # sq01.enqueue(2)
    # sq01.enqueue(3)
    # print(sq01.is_empty())
    # print(sq01.dequeue())

    # 想要完成队列里的元素的反转就要用到栈的模型
    from demo01_sstack import *

    # 循环出队入栈
    st01 = SStack()
    while not sq01.is_empty():
        st01.push(sq01.dequeue())

    # 循环出栈入队
    while not st01.is_empty():
        sq01.enqueue(st01.pop())

    # 打印
    while not sq01.is_empty():
        print(sq01.dequeue())
