# author: Ziming Guo
# time: 2020/3/8
"""
给出两个有序的链表L1,L2 .
在不创建新的链表的基础上将两个链表合并为一个
要求合并后的链表仍为有序
"""

from linklist_edited import *

# 创建两个链表,初始化数值
L1 = LinkList()
L2 = LinkList()

L1.init_list([1, 5, 7, 8, 10, 12, 13, 19])
L2.init_list([0, 3, 4, 8, 14, 21, 22])

L1.show()
print("=========================")
L2.show()


def merge(L1, L2):
    # 将L2向L1中合并
    p = L1.head
    q = L2.head.next
    while p.next is not None:
        if p.next.val < q.val:
            p = p.next # 表示 p 向后走一个位置
        else:
            tmp = p.next # 先做一个标记，防止丢失
            p.next = q # 让p的下一个节点指向q，这一步只是指向的，没有往下走，单纯的指向
            p = p.next # 让p往下走一个单位，相当于到了原来的p
            q = tmp # 让q指向做了标记的点

    p.next = q # 循环完毕，即 直到下一个为空了，让下一个等于q


merge(L1, L2)
print("=================================")
L1.show()
