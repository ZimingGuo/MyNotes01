# author: Ziming Guo
# time: 2020/2/22
"""
     练习1：
     repr & str & eval
     创建Enemy类对象，将对象打印在控制台中(格式自定义)
     克隆Enemy类对象，体会克隆对象变量的改变不影响原对象。

class Enemy:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
"""


class Enemy:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def __str__(self):
        return "我这有一个敌人，他叫%s，血量是%d，攻击力是%d，防御力是%d" % (self.name, self.hp, self.atk, self.defense)

    def __repr__(self):
        return "Enemy('%s',%d,%d,%d)" % (self.name, self.hp, self.atk, self.defense)
        # 注意名字的字符串那个地方用的是单引号，而不是双引号


e01 = Enemy("哈哈", 100, 200, 800)
print(e01)
str01 = str(e01)
print(e01)
print(str01)

str02 = repr(e01)  # 把对象转换成特定字符串
print(str02)
clone01 = eval(str02)  # 将字符串直接执行了（eval方法就有这个功能）(也就是完全复制了一个对象)
print(clone01)
clone01.name = "qwert"
print(clone01)
