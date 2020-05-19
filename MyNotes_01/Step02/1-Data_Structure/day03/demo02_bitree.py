# author: Ziming Guo
# time: 2020/3/12
"""
demo02:
    bitree.py  二叉树的遍历实践
    用编程的思想和方式实现树形结构的先序，中序，后序

思路分析:
1. 使用链式结构存储二叉树的节点数据
2. 节点中存储 数据, 左孩子链接,右孩子链接 三个属性
"""
from _squeue import *


# indicate: 要保证每一个模块里的方法名称和老师一样，这样保证调用的时候不会出问题


# 二叉树节点类，其实就是原来的那个 node 节点，多了一个接口
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left  # 左节点表示左树杈
        self.right = right  # 右节点表示右树杈


# 二叉树遍历方法
class Bitree:
    def __init__(self, root):
        self.root = root  # 在初始化的时候，首先传入开始遍历的节点（遍历的起始位置）

    # 先序遍历
    def preOrder(self, node):
        """
            起始对每一个节点的操作都有一个固定的模式，所以可以用递归思想
            如果遇到了两个叶子都是 None 的情况，就会返回上一层，层层返回
        :param node:
        :return:
        """
        if node is None:  # 终止条件
            return # 这个 return 指的是 return 到了父节点
        print(node.val)  # 打印节点的数据
        self.preOrder(node.left)  # 打印左节点的数据
        self.preOrder(node.right)  # 打印右节点的数据

    # 中序遍历
    def inOrder(self, node):
        if node is None:
            return
        self.inOrder(node.left)
        print(node.val)
        self.inOrder(node.right)

    # 后序遍历
    def postOrder(self, node):
        if node is None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.val)

    # 　层次遍历
    def levelOrder(self, node):
        """
        让初始节点先入队，谁出队就遍历谁
        同时让出队元素的左右孩子入队，直到队列为空
        """
        sq = SQueue() # 创建对象
        sq.enqueue(node) # 让第一个节点入队
        while not sq.is_empty(): # 只要不是空
            node = sq.dequeue()
            print(node.val)  # 遍历元素
            if node.left:
                sq.enqueue(node.left) # 如果左节点不为 None，就入左节点
            if node.right:
                sq.enqueue(node.right) # 如果右节点不为 None，就入右节点


if __name__ == '__main__':
    # 下面的代码是根据后序遍历构建二叉树
    # 先从叶子写起，这样根的部分就比较好表示了
    b = Node('B')
    f = Node('F')
    g = Node('G')
    d = Node('D', f, g)
    h = Node('H')
    i = Node('I')
    e = Node('E', h, i)
    c = Node('C', d, e)
    a = Node('A', b, c)  # 整个树根
    # 和之前的方式有所不同：
    # 这次并没有把树的建立写成一个函数的形式，而是零散的语句，通过使用 Node 节点，手动建立

    bt = Bitree(a)  # 把a作为根节点进行遍历

    bt.preOrder(bt.root)
    print("========================")
    bt.inOrder(bt.root)
    print("========================")
    bt.postOrder(bt.root)
    print("========================")
    bt.levelOrder(bt.root)
