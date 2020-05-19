# author: Ziming Guo
# time: 2020/2/27
"""
    练习2:
        定义生成器函数my_zip,实现下列现象.
        将多个列表的每个元素合成一个元组.
        list02  = ["孙悟空","猪八戒","唐僧","沙僧"]
        list03  = [101,102,103,104]
        for item in zip(list02,list03):
            print(item)
"""


def my_zip(list_former, list_later):
    length = 0
    times = 0
    if len(list_later) > len(list_former):
        length = len(list_former)
    else:
        length = len(list_later)
    while times < length:
        for i in range(0, length):
            list_inner = []
            list_inner.append(list_former[i])
            list_inner.append(list_later[i])
            print(tuple(list_inner))  # 这句话就是能够转换成元组的
            times += 1


list02 = ["孙悟空", "猪八戒", "唐僧", "沙僧"]
list03 = [101, 102, 103, 104]
my_zip(list02, list03)
