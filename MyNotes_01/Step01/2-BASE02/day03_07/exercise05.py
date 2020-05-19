# author: Ziming Guo
# time: 2020/2/10
'''
    练习5：
    列表排序(升序小　-->  大)
    [3,80,45,5,7,1]
    目标:列表中所有元素两两比较
    思想:
    　取出第一个元素,与后面元素进行比较.
    　取出第二个元素,与后面元素进行比较.
    　取出第三个元素,与后面元素进行比较.
      ...
      取出倒数第二个元素,与后面元素进行比较.
      如果取出的元素大于(>)后面的元素,
          则交换
'''
list01 = [3, 80, 45, 5, 7, 1]

for m in range(len(list01)-1): # 取数据

    for i in range(m + 1, len(list01)): # 做比较
        if list01[m] > list01[i]:  # 降序的情况就是换这个比较符号
            list01[m], list01[i] = list01[i], list01[m]

print(list01)

# 这是一个元素排列问题的基本思想
# 取出第一个元素，和之后的元素，两两相互比较
# 升序：如果后面元素小于此元素，交换
# 降序：如果后面元素大于此元素，交换

# 写两层 for 循环的问题中，找规律，先写里面一层，再写外面的一层

# 老师的课堂笔记
'''
    取出第一个元素,与后面元素进行比较
    list01[0]  list01[1]
    list01[0]  list01[2]
    list01[0]  list01[3]
    for c in range(1,len(list01)):
        # list01[0]  list01[c]
        pass
    取出第二个元素,与后面元素进行比较
    for c in range(2,len(list01)):
        # list01[1]  list01[c]
        pass
    取出第三个元素,与后面元素进行比较
    for c in range(3,len(list01)):
        # list01[2]  list01[c]
        pass
'''