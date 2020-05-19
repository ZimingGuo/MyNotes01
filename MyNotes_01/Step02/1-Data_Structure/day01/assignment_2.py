# author: Ziming Guo
# time: 2020/3/8
from linklist_edited import *

link01 = LinkList()
link02 = LinkList()
l01 = [1, 2, 3, 7, 8]
l02 = [4, 5, 6, 9]

link01.init_list(l01)
link02.init_list(l02)

p01 = link01.head
p02 = link02.head
p03 = link01.head
p04 = link02.head
p05 = link01.head
p06 = link02.head

for i in range(len(l01)):  # 获取 link01 的最后一个元素
    p01 = p01.next
    # print(p01)

for i in range(len(l02)):  # 获取 link02 的最后一个元素
    p02 = p02.next

p01.next = p02
# 要让 link01 的最有一个元素的 next 属性指向 link02 最后一个元素
# 加上了第二段


for i in range(3):  # 获取 link02 里的"6"元素
    p04 = p04.next

for i in range(4):  # 获取 link01 里的"7"元素
    p03 = p03.next

p04.next = p03  # 让link02 里的"6"元素指向link01 里的"7"元素

for i in range(3):  # 获取 link01 里的"3"元素
    p05 = p05.next

p05.next = p06.next # link01中的"3"元素连接link02中的第一个4元素

link01.show()

# print("==================================")
# print(link01.search(4))
# link01.to_insert01
