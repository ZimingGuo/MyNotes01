# author: Ziming Guo
# time: 2020/2/22
'''
     练习2:
     重载运算符
     实现自定义类的对象与数值的减法，乘法运算。
'''


class Vector:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return "%d哈哈哈啊哈" % (self.x)

    def __add__(self, other):
        add01 = self.x + other
        self.x += other
        return add01, self.x, Vector(self.x + other)

    def __sub__(self, other):  # 现在 self.x 是14
        sub01 = self.x + other  # 24
        sub02 = self.x - other  # 4
        self.x -= other  # 4 # 现在 self.4 是4
        return sub01, sub02, self.x

    def __radd__(self, other):
        return self.x + other


# 测试代码
v01 = Vector(2)
re01 = v01.__add__(10)  # (12,12,还有一个新创建的对象 )
print(re01[0])  # 12
print(re01[1])  # 12
print(v01 + 2)  # 14

print(str(re01[2]))  # 22哈哈哈啊哈
# 打印的是：一个新的对象，然后变成了字符串，新的 Vector 对象的赋值为22，因为在创建这个对象在以前 self.x 已经被更改值了

print(str(v01))  # 旧的字符串，调用了 str 方法
print(v01)  # 旧的字符串调用了 str 方法

r03 = v01.__sub__(10)  # (24,14,4)
print(r03)
print(v01 - 2)  # 表示实行 v01.__sub__(2)方法 先是一个加再是一个减，最后一个增强减 # 此时 self.x 是 2

r04 = v01.__radd__(2)
print(2 + v01)
print(str(2 + v01))
print(v01)
