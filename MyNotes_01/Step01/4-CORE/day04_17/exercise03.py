# author: Ziming Guo
# time: 2020/2/27
'''
    练习3:
        1. 获取列表中所有字符串
        2. 获取列表中所有小数
        要求:分别使用生成器函数/生成器表达式/列表推导式完成.
        list01 = [3, "54", True, 6, "76", 1.6, False, 3.5]
'''

list01 = [3, "54", True, 6, "76", 1.6, False, 3.5]


# 练习1 ：找字符串
# 生成器函数
def get_str_generator_fun(list_target):
    for item in list_target:
        if type(item) == str:
            yield item


result01 = get_str_generator_fun(list01)
for item01 in result01:
    print(item01)

# 生成器表达式
result02 = (item for item in list01 if type(item) == str)
for item02 in result02:
    print(item02)

# 列表推导式
result03 = [item for item in list01 if type(item) == str]
for item03 in result03:
    print(item03)
# 调试的时候你就会发现，这个列表推导式在执行的过程中，是在一直执行这一句话
# 直到把所有结果全都找出来之后，存在一个列表里面
# 最后再遍历这个列表里面的每一个元素，把它们取出来
# 而之前的有关生成器的方法都是 做一个 拿走一个 释放一个


# 练习2：找小数
# 生成器函数
def get_str_generator_fun(list_target):
    for item in list_target:
        if type(item) == float:
            yield item


result01 = get_str_generator_fun(list01)
for item01 in result01:
    print(item01)

# 生成器表达式
result02 = (item for item in list01 if type(item) == float)
for item02 in result02:
    print(item02)

# 列表推导式
result03 = [item for item in list01 if type(item) == float]
for item03 in result03:
    print(item03)
