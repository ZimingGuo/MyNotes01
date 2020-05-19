# author: Ziming Guo
# time: 2020/3/6
"""
demo01_linklist.py
    功能: 实现单链表的构建和操作
    重点代码
    其实以下这些 类里面的实例方法 都是在实现类似于列表的 append insert remove 等等操作
    只不过现在是对链表进行操作
"""


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
        val 是我们要的货真价实的有用数据；next 从数据上看是没有用的，但是是用来建立关系的
        val: 有用数据；每创建一个 Node 都会创建一个 val，这是数据
        next: 下一个节点引用
        """
        self.val = val
        self.next = next
        # next 就相当于这个类里面有一个属性，而这个属性的值，又是这个类的对象


# 链式线性表操作类
class LinkList:
    """
    思路 : 生成单链表,通过实例化的对象就代表一个链表
          可以调用具体的操作方法完成各种功能
    """

    def __init__(self):
        # 链表的初始化节点,没有有用数据,但是便于标记链表的开端
        # head 也是一个节点，只不过里面没有数据
        # 但是结构和 Node 是一样的，因为也是一个 Node 类的对象
        # 表头：以后的所有后续操作都要以这个表头没基准进行操作
        self.head = Node(None)

    # 初始化链表,添加一组节点
    def init_list(self, list_):
        p = self.head  # p 作为移动变量，把p定义成为了表头
        for item in list_:
            # 遍历到一个值就创建一个节点
            p.next = Node(item)  # 创建了一个对象
            p = p.next  # 再往后走一步

    # 遍历链表
    def show(self):
        p = self.head.next  # p代表第一个有值的节点
        while p is not None:
            print(p.val)
            p = p.next  # p向后移动

    # 判断链表为空
    def is_empty(self):
        """
            如果头的 next 位置为空，就证明没有后续内容了
        :return: 是否为空链表
        """
        if self.head.next is None:
            return True
        else:
            return False

    # 清空链表
    def clear(self):
        """
            晴空链表就是说只有一个 head 表头，没啥了
            但实际上这只是把表头 head 和后面的数据分开了，但是后面的内容还是存在的
            python 有自己的垃圾处理机制，当这些数据没有被赋值，就会被销毁
        """
        self.head.next = None

    # 尾部插入
    def append(self, val):
        """
            一般不太喜欢在尾部增加，因为需要遍历到尾部才能进行操作
            实际效率并不高
        :param val:要插入的数据
        """
        p = self.head
        # p移动到最后一个节点
        while p.next is not None:
            p = p.next
        p.next = Node(val)  # 最后添加节点

    # 头部插入
    def head_insert(self, val):
        """
        思想：1）生成节点
             2）让要节点的 next 指向 head 的 next
             3）让 head 的 next 指向新生成的这个要插入的 node
             注意：这三部的顺序是不能点颠倒的，以防后面数据找不到
        :param val: 要插入的数据
         """
        node = Node(val)  # 1）
        node.next = self.head.next  # 2）
        self.head.next = node  # 3）

    # 指定位置插入
    def insert(self, index, val):
        """
        首先要定义一个变量，让它走到你要插入变量的位置的前一个位置
        然后先用Node来指向下一个的next，上一个指向这个新的 Node
        注意：数据少的情况下这样插入时间差不多，但是如果数据很多很多的话，要一个一个遍历，所以耗时就会较长
        :param index: 要插入的位置
        :param val: 要插入的数据值
        """
        # 设置个p 移动到待插入位置的前一个
        p = self.head
        for i in range(index):
            # 如果index超出了最大范围跳出循环
            if p.next is None:
                break
            p = p.next
        # 插入节点，这三步就是必要的倒腾的过程
        node = Node(val)
        node.next = p.next
        p.next = node

    # 删除节点
    def remove(self, val):
        """
            根据数据值删除一项
            删除的原理：移除中间（要删除的）一项，让前后两项相连就可以，不用管中间那项去哪了
        :param val: 要删除的那一项的数据的值
        """
        p = self.head
        # p 移动,待删除节点上一个
        while p.next is not None and p.next.val != val: # 这两个条件的顺序不能换，先判断是否有，有再判断下一个
            p = p.next
        # 当用 while 判断循环条件的时候，之后一定要判断一下是因为哪个因素结束了循环
        if p.next is None:
            raise ValueError("x not in linklist")
        else:
            p.next = p.next.next

    # 获取某个节点的值 (通过索引获取)
    def search(self, index):
        if index < 0:
            raise IndexError("index out of range")

        p = self.head.next # 这代表第一个有用值
        # 循环移动p
        for i in range(index):
            if p is None:
                raise IndexError("index out of range")
            p = p.next
        return p.val


if __name__ == "__main__":
    # 想有一个链表
    link = LinkList()

    # 初始化一组数据，就是把列表里面的各个元素作为链表的每一项插进去
    l = [1, 2, 3, 4]
    link.init_list(l)
    link.clear()
    print(link.search(0))

    # 链表遍历
    # link.show()
    # link.insert(2,88)
    # link.show()

    # link.clear()
    # print(link.is_empty())

# Abby = Node((1,'Abby',18,'w'))
# Emma = Node((2,'Emma',17,'w'))
# Alex = Node((3,'Alex',19,'m'))
#
# Abby.next = Emma
# Emma.next = Alex
