# author: Ziming Guo
# time: 2020/3/7
# 创建节点类
class Node:
    """
    思路 : *自定义类视为节点类,类中的属性为数据内容
          *写一个next属性,用来和下一个 节点建立关系
          特点就是：给一个类赋值，但是赋的这个值仍然是这这个类的一个对象
          即：实例对象里面的一个属性，这个属性的值仍然是同一类型的实例对象
    """

    def __init__(self, val, next=None):
        """
        val: 有用数据
        next: 下一个节点引用
        """
        self.val = val
        self.next = next


# 链式线性表操作类
class LinkList:
    """
    思路 : 生成单链表,通过实例化的对象就代表一个链表
          可以调用具体的操作方法完成各种功能
    """

    def __init__(self):
        # 链表的初始化节点,没有有用数据,但是便于标记链表的开端
        self.head = Node(None)

    # 初始化链表,添加一组节点
    def init_list(self, list_):
        p = self.head
        for itme in list_:
            p.next = Node(itme)

    # 在指定位置插入节点
    def insert_somewhere(self, value, place):
        node_target = Node(value)
        p = self.head
        for i in range(place - 1):
            p = p.next
        node_target.next = p.next
        p.next = node_target
