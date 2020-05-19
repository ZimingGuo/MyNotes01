# author: Ziming Guo
# time: 2020/3/8
"""
demo01_sstack.py  栈模型的顺序存
重点代码

思路 :
1. 顺序存储可以使用列表实现,但是列表功能丰富,不符合栈模型要求
2. 将列表功能封装,实现顺序栈的类,只提供栈的操作功能

功能: 出栈, 入栈,判断栈空,查看栈顶元素
"""


# 自定义异常
class StackError(Exception):
    pass


# 顺序栈
# 顺序栈不同于链式栈，顺序栈需要一个列表，一个一个往里面加东西
# 链式栈是在内存里随便找地方，所以需要的是 Node 而不是列表
class SStack:
    def __init__(self):
        # 空列表就是栈的存储空间
        # 列表的最后一个元素作为栈顶元素
        # 下面的实例方法就是对方法的封装
        self.__elems = []

    # 入栈
    def push(self, val):
        self.__elems.append(val)

    # 判断栈空
    def is_empty(self):
        """
            python 的主要特点就是简洁优雅
            这样写好处就是简练，直接输出的就是 bool 值，很好
        :return: 输出栈是否为空的 bool 值
        """
        return self.__elems == []

    # 出栈
    def pop(self):
        """
            出栈只能从最后一个位置弹出来
        :return: 弹出来一个值
        """
        if self.is_empty():
            raise StackError("pop from empty stack")
        return self.__elems.pop()

    # 查看栈顶
    def top(self):
        """
            只是简单的查看，而不是弹出
        :return: 只是返回值，而不是弹出来，外面是接受不到的
        """
        if self.is_empty():
            raise StackError("pop from empty stack")
        return self.__elems[-1] # 把最后一个元素位置看作是栈顶，所以是[-1]


if __name__ == '__main__':
    st = SStack()  # 实例化一个栈的对象（创建一个对象）
    st.push(10)
    st.push(20)
    st.push(30)
    while not st.is_empty():
        print(st.pop())
    st.pop()
