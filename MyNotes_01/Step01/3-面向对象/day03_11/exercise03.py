# author: Ziming Guo
# time: 2020/2/17
'''
    练习03：
    使用方法封装变量，还是封装练习2的那个敌人类
    使用 @property 封装变量
'''


class Enemy:
    def __init__(self, name, attack, blood):
        self.name = name
        self.attack = attack
        self.blood = blood

    @property  # 创建property对象，只负责拦截读取操作
    def attack(self):
        return self.__attack

    @attack.setter  # 只负责拦截写入操作
    def attack(self, value):
        if value > 50 or value < 10:
            raise ValueError("attack 不行不行！")
        else:
            self.__attack = value

    @property
    def blood(self):
        return self.__blood

    @blood.setter
    def blood(self, value):
        if value > 200 or value < 100:
            raise ValueError("blood 不行不行！")
        else:
            self.__blood = value


list_enemy = [
    Enemy(1, 40, 140),
    Enemy(2, 30, 150),
]

print(list_enemy[0].attack, list_enemy[0].blood)
print(list_enemy[1].attack, list_enemy[1].blood)

# list_enemy[0].set_blood(199)
# list_enemy[1].set_attack(49)
# print(list_enemy[0].blood)
# print(list_enemy[0].attack) # 这两句话不能执行是因为
# blood 和 attack 是两个隐藏变量
# 无法直接访问
# print(list_enemy[0].get_blood())
# print(list_enemy[0].get_attack())

b01 = Enemy(1, 25, 150)
print(b01.attack)
print(b01.name, b01.attack, b01.blood)  # 这种方式封装之后，可以随时访问 / 调用隐藏变量
# 之前的第一种封装方式不可以直接调用隐藏变量
b01.blood = 120  # 直接调用方法 & 更改隐藏变量
b01.attack = 20  # 直接调用方法 & 更改隐藏变量
print(b01.name, b01.attack, b01.blood)
