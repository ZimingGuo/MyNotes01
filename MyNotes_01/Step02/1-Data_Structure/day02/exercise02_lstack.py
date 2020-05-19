# author: Ziming Guo
# time: 2020/3/9
'''
    练习2：
    自己再次实现一个链式栈
'''


# 自定义异常
class StackError(Exception):
    pass


# 节点类
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# 开始定义
class LinkStack:
    def __init__(self):
        self._top = None

    def push(self, value):
        """
            压栈
        :param value: 压入栈的值
        """
        node = Node(value)
        node.next = self._top
        self._top = node

    def pop(self):
        """
            弹栈操作
        :return: 弹出的栈顶
        """
        if self._top is None:
            raise StackError("这是一个空栈，无数据可pop")
        result = self._top
        self._top = self._top.next
        return result

    def check(self):
        """
            仅是查看栈顶，而不是弹栈
        :return: 栈顶元素
        """
        if self._top is None:
            raise StackError("pop from empty stack")
        return self._top.val
