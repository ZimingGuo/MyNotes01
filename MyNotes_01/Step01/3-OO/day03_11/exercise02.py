# author: Ziming Guo
# time: 2020/2/16
'''
    练习02：
    用第二种方法封装变量 (property方法)
    定义敌人类(姓名，攻击力10 -- 50，血量100 -- 200)
    创建一个敌人对象，可以修改数据，读取数据。
'''


# 使用方法封装变量
class Enemy:
    def __init__(self, name, attack, blood):
        self.name = name
        self.attack = attack
        self.blood = blood
        # 虽然在这两个地方写了 attack 和 blood，但是实际上，这两个并不是数据
        #   而是类变量，类变量指向的是 property 对象
        #   真实操作的数据都是带两个下划线的

        # self.set_attack(attack)
        # self.set_blood(blood)

    def get_attack(self):
        return self.__attack

    def set_attack(self, value):
        if value > 50 or value < 10:
            raise ValueError("attack 不行不行！")
        else:
            self.__attack = value

    # 进行拦截（创建了一个类变量）
    attack = property(get_attack, set_attack)

    # 用这个来拦截对 attack 变量的读写操作

    def get_blood(self):
        return self.__blood

    def set_blood(self, value):
        if value > 200 or value < 100:
            raise ValueError("blood 不行不行！")
        else:
            self.__blood = value

    # 进行拦截（创建了一个类变量）
    blood = property(get_blood, set_blood)
    # 用这个来拦截对 blood 变量的读写操作

    # blood = property(None, set_blood) # 只写属性
    # blood = property(get_blood,None) # 只读属性


list_enemy = [
    Enemy(1, 40, 140),
    Enemy(2, 30, 150),
]

print(list_enemy[0].get_attack())
print(list_enemy[0].get_blood())
print(list_enemy[1].get_attack())
print(list_enemy[1].get_blood())

# list_enemy[0].set_blood(199)
# list_enemy[1].set_attack(49)
# print(list_enemy[0].blood)
# print(list_enemy[0].attack) # 这两句话不能执行是因为
# blood 和 attack 是两个隐藏变量
# 无法直接访问
# print(list_enemy[0].get_blood())
# print(list_enemy[0].get_attack())

b01 = Enemy(1, 25, 150)
print(b01.name, b01.attack, b01.blood)
b01.blood = 120
b01.attack = 220
print(b01.name, b01.attack, b01.blood)
