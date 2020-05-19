# author: Ziming Guo
# time: 2020/3/9
"""
demo02_lstack.py 栈的链式模型
lstack 的意思就是链式栈 linkstack
重点代码
    思路:
        1. 通过节点存储数据达到链式存储的目的
        2. 封装方法,实现栈的基本操作(入栈,出栈,栈空,查看栈顶)
        3. top为栈顶,在链表的头作为栈顶位置 (不许要遍历)
"""


# 自定义异常
class StackError(Exception):
    pass


# 节点类
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# 链式栈模型
class LStack:
    def __init__(self):
        # top作为栈顶的标记
        # 没有元素的时候 top 指向 None；有元素的话它就指向这个元素，且永远指向最新的那个元素
        self.__top = None

    def is_empty(self):
        return self.__top is None

    # 入栈
    def push(self, val):
        self.__top = Node(val, self.__top)
        # 这句话就是用到了 Node 的第二个参数
        # 直接让所创建的这个节点的下一个位置指向 top
        # 然后再让 top 移动到现在的这个节点上来

        # node = Node(val) 先有一个节点
        # node.next = self.__top 节点的下一个指向当前的 top
        # self.__top = node 然后再把 top 移动到这个节点上

    # 出栈
    def pop(self):
        if self.__top is None:
            raise StackError("pop from empty stack")
        data = self.__top.val  # 不能直接 return 当前节点的 value，因为先 return 的话就没办法移动 top 了
        self.__top = self.__top.next
        return data

    # 查看栈顶元素
    def top(self):
        if self.__top is None:
            raise StackError("pop from empty stack")
        return self.__top.val


if __name__ == '__main__':
    ls = LStack()
    ls.push(10)
    ls.push(20)
    ls.push(30)
    print(ls.pop())
    print(ls.pop())
