# author: Ziming Guo
# time: 2020/3/9
'''
    练习5：
    自己再把lqueue写一遍
    思路:
        1. 基于链表构建队列模型
        2. 链表的开端作为队头, 结尾作为队尾
        3. 对头队尾分别添加标记,避免每次插入数据都遍历链表
        4. 队头和队尾重叠时认为队列为空
'''


# 自定义异常
class QueueError(Exception):
    pass


# 节点类
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkQueue:
    def __init__(self):
        self.front = self.rear = Node(None)

    # 判读是否为空
    def is_empty(self):
        return self.front == self.rear

    # 在 rear 后增加元素
    def intoqueue(self, value):
        node = Node(value)
        self.rear.next = node
        self.rear = self.rear.next

    # 在队列里面拿出元素
    def outofqueue(self):
        if self.is_empty():
            raise QueueError("Queue is empty")
        self.front = self.front.next
        return self.front.val
