# author: Ziming Guo
# time: 2020/2/27
"""
    练习1:
        定义生成器函数my_enumerate,实现下列现象.
        将元素与索引合成一个元组.
list01 = [3, 4, 55, 6, 7]
for item in enumerate(list01):
    # (索引,元素)
    print(item)

for index, element in enumerate(list01):
    print(index, element)
"""

list01 = [3, 4, 55, 6, 7]


def my_enumerate(iterable_target):
    index01 = 0
    for item in iterable_target:
        output = (index01, item)
        yield output
        index01 += 1


result01 = my_enumerate(list01)
for item in result01:
    print(item)
