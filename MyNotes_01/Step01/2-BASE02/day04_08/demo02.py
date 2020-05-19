# author: Ziming Guo
# time: 2020/2/10
'''
    demo02：
    返回值的应用
'''
# 设计思想：分而治之
#         干一件事

# 需求：定义两个数字相加的函数（这两个数不一定就是在控制台里获取的，还可能是从元组 or 列表里获取的）
#
# def add():
#     1. 获取数据
#     number01 = int(input("请输入第一个数字："))
#     number02 = int(input("请输入第二个数字："))
#     2. 逻辑计算
#     result = number01 + number02
#     3. 显示结果
#     print(result)
#
# add()

def add(number01, number02):  # 这才叫只做一件事
    # 逻辑处理
    return number01 + number02


# 调用者提供数据
#   数据从何而来与定义函数的人没有关系
#   用函数的人决定数据从何而来
number01 = int(input("请输入第一个数字："))
number02 = int(input("请输入第二个数字："))
result = add(number01, number02)
# 调用者负责显示结果
print("结果是:" + str(result))

# 函数的设计者只做一件事：逻辑思想
