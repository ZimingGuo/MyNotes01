# author: Ziming Guo
# time: 2020/3/13
"""
    练习1：冒泡排序
    实现把列表里的数据从大到小进行排序
    方法就是双 for 循环，逐个进行交换
"""

# 冒泡排序：双层循环
def bubble(list_):
    for m in range(0, len(list_) - 1):
        for n in range(m + 1, len(list_)): # 注意这个地方一定是从 m 开始的
            if list_[m] > list_[n]:
                list_[m], list_[n] = list_[n], list_[m]


l = [4, 9, 3, 1, 2, 5, 8, 4]
bubble(l)
print(l)
