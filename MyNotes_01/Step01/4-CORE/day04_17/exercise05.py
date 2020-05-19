# author: Ziming Guo
# time: 2020/2/28
'''
    练习5：
    1. 使用生成器函数实现以上3个需求
    2. 体会函数式编程的"封装"
       将三个函数变化点提取到另外三个函数中.
       将共性提取到另外一个函数中
    3. 体会函数式编程的"继承"与"多态"
       使用变量隔离变化点,在共性函数中调用变量.
    4. 测试(执行上述功能)
'''
list01 = [43, 4, 5, 5, 6, 7, 87]


# 需求1:在列表中查找所有偶数
def get_even(list_target):
    for item in list_target:
        if item % 2 == 0:
            yield item


for item in get_even(list01):
    print(item)

print("--------------------------------------------")


# 需求2:在列表中查找所有大于10的数
def get_above_10(list_target):
    for item in list_target:
        if item > 10:
            yield item


for item in get_above_10(list01):
    print(item)

print("--------------------------------------------")


# 需求3:在列表中查找所有范围在10--50之间的数
def get_range_1050(list_target):
    for item in list_target:
        if item > 10 and item < 50:
            yield item


for item in get_range_1050(list01):
    print(item)

print("--------------------------------------------")


# "封装"
def condition_even(item):
    return item % 2 == 0


def condition_above_10(item):
    return item > 10


def condition_range_1050(item):
    return item > 10 and item < 50


# "继承"与"多态"
def get_element(func_condition, list_target):
    for item in list_target:
        if func_condition(item):
            yield item


# 执行功能
for item in get_element(condition_even, list01): # 现在是想把函数传进去，而不是调用函数，所以不要加括号 
    print(item)

print("--------------------------------------------")

for item in get_element(condition_above_10, list01):
    print(item)

print("--------------------------------------------")

for item in get_element(condition_range_1050, list01):
    print(item)
