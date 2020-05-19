# author: Ziming Guo
# time: 2020/2/21
"""
    demo01：
    内置可重写函数
    练习:exercise02.py
"""


class StudentModel:
    def __init__(self, name="", age=0, score=0, id=0):
        self.name = name
        self.age = age
        self.score = score
        self.id = id

    # 对象 --> 字符串 (随意格式)
    # 把对象变成了字符串，等再打印对象的时候，就直接打出来一个字符串了
    # 虽然这是一个方法，但是实际上不用调用，创建出来之后，再打印对象，直接就是字符串了
    def __str__(self):
        return "我叫%s,编号是%d,年龄是%d,成绩是:%d" % (self.name, self.id, self.age, self.score)

    # 对象 --> 字符串(解释器可识别,有格式)
    # str 可以直接输出用，而 repr 就要对创建的对象进行操作
    def __repr__(self):
        return "StudentModel('%s',%d,%d,%d)" % (self.name, self.age, self.score, self.id)


s01 = StudentModel("无忌", 27, 100, 101)  # 创建了一个对象
str01 = str(s01)  # 只有在类里面创建了 str 内置方法，才能转换成字符串
# 调用 str 方法，用 str 方法处理对象 s01
# 如果不在类里面添加 str 内置方法的话 输出的都不是字符串
print(str01)
print(s01)

str02 = repr(s01)
print(str02)

# 根据字符串执行python代码
re = eval("1+2*5")
# exec
print(re)

# 克隆对象
# repr 返回python格式的字符串
# eval根据字符串执行代码
s02 = eval(repr(s01))
# 这句话的克隆原理就是：先把对象转换成一个固定格式的字符串(repr)
# 然后再用 eval 方法把字符串转换成 python 代码
# 然后给一个变量，就克隆出来了
s02.name = "老张"
print(s01.name)
