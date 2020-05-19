# author: Ziming Guo
# time: 2020/2/26
'''
    练习7——edited:
        从列表[4,5,566,7,8,10]中选出所有偶数
        -- 结果存入另外一个列表中
        -- 使用生成器实现
'''
list01 = [4, 5, 566, 7, 8, 10]


def get_even01():
    result = []
    for item in list01:
        if item % 2 == 0:
            result.append(item)
    return result


re = get_even01()
for item in re:
    print(item)


def get_even02():
    for item in list01:
        if item % 2 == 0:
            yield item

# 当二者都写成函数的形式之后，就会发现
#       第二种方法是那一个数据存储一个数据，并且释放上一个数据
#       而不是把所有数据判断完之后放在一个列表里面
g01 = get_even02()
for item in g01:
    print(item)
