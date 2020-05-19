# author: Ziming Guo
# time: 2020/2/11
'''
    练习10：
    定义函数：让所有数值相加在一起
'''

core = 0


def add_all(*args):
    for item in args:
        global core
        core += item
    return core


result = add_all(1, 3.2, 5, 2, 5)
print(result)
