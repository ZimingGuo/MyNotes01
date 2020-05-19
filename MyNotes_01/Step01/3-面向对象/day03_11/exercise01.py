# author: Ziming Guo
# time: 2020/2/16
'''
    练习1:
    定义敌人类(姓名，攻击力10 -- 50，血量100 -- 200)
    创建一个敌人对象，可以修改数据，读取数据。
'''

# 使用方法封装变量
class Enemy:
    def __init__(self, name, attack, blood):
        self.name = name
        # self.__attack = attack
        # self.__blood = blood
        # 如果按照这种方式定义变量，只是能防止在下面的程序中，用 set 设置变量值的时候
        #   防止设置的值超出范围，但是从 __init__ 方法进入的时候，还是会超出范围值

        self.set_attack(attack)
        self.set_blood(blood)
        # 用这两种方式设置初始值的时候，就避免了上面说的问题，可以从开始就避免值超过范围

    # 定义读数据的方法
    def get_attack(self):
        return self.__attack # 返回的是隐藏的值

    # 定义写数据的方法
    def set_attack(self, value):
        if value > 50 or value < 10:
            raise ValueError("attack 不行不行！")
        else:
            self.__attack = value # 设置的是隐藏的值

    # 定义读数据的方法
    def get_blood(self):
        return self.__blood # 返回的是隐藏的值

    # 定义写数据的方法
    def set_blood(self, value):
        if value > 200 or value < 100:
            raise ValueError("blood 不行不行！")
        else:
            self.__blood = value # 设置的是隐藏的值


list_enemy = [
    Enemy(1, 40, 140),
    Enemy(2, 30, 150),
]

print(list_enemy[0].get_attack())
print(list_enemy[0].get_blood())
print(list_enemy[1].get_attack())
print(list_enemy[1].get_blood())

list_enemy[0].set_blood(199)
list_enemy[1].set_attack(49)
# print(list_enemy[0].blood)
# print(list_enemy[0].attack) # 这两句话不能执行是因为
                              # blood 和 attack 是两个隐藏变量
                              # 无法直接访问
print(list_enemy[0].get_blood())
print(list_enemy[0].get_attack())
