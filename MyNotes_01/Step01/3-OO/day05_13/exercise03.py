# author: Ziming Guo
# time: 2020/2/21
"""
    练习3：
    手雷炸了，可能伤害敌人/玩家的生命.
             还可能伤害未知事物(鸭子.房子....)
    要求：增加了新事物，不影响手雷。
    体会：继承的作用
         多态的体现
         设计原则
            开闭原则
            单一职责
            依赖倒置
    画出设计图
    15:35
"""


class Grenade:
    def __init__(self, name, atk):
        self.name = name
        self.atk = atk

    def boom(self, damage_target):
        print(self.name, "爆炸啦！")
        # 调用 玩家 鸭子 房子，那是我只能调用他们的代表，即他们的父类
        damage_target.damage(self.atk)


class Damageable:
    """
        可以受伤
    """

    def damage(self, value):
        pass  # 这里不能写具体的细节，要是有共性可以写共性


# --------------------------- 架构师工作 over -----------------------------

class Duck(Damageable):
    def __init__(self, hp):
        self.hp = hp

    def damage(self, value):
        self.hp -= value
        print("伤害了大鸭子，大鸭子受伤了! 剩余血量：", self.hp)


class House(Damageable):
    def __init__(self, hp):
        self.hp = hp

    def damage(self, value):
        self.hp -= value
        print("伤害了大房子，大房子受伤了剩余血量：", self.hp)


g01 = Grenade("大炸弹", 100)
d01 = Duck(500)
h01 = House(10000)

g01.boom(d01)
g01.boom(h01)
 # 此处体现了 创建一个列表装所有子类 的优点
 # 上面这段代码是没有建立列表的，分别对两个对象(大鸭子 & 大房子)进行操作
 # 如此操作就需要两补：先伤害大鸭子，再伤害大房子
 # 但是如果做成列表并添加受害者，就可以直接遍历列表，一步伤害就可以对列表里的所有受害者进行伤害
