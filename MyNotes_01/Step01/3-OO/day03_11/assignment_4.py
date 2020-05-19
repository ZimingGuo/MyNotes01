# author: Ziming Guo
# time: 2020/2/17
'''
    作业4：
    请用面向对象思想，描述以下场景：
    玩家(攻击力)攻击敌人(血量)，敌人受伤(掉血)，还可能死亡(掉装备，加分)。
    敌人(攻击力)攻击玩家，玩家(血量)受伤(掉血/碎屏),还可能死亡(游戏结束)。
'''


# 玩家：攻击力，血量
# 敌人：攻击力，血量


class Player:
    def __init__(self, name, atk, hp):
        self.name = name
        self.atk = atk
        self.hp = hp

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        self.__atk = value

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value

    def fire_enemy(self, enemy):  # 表示袭击了一个敌人
        enemy.hp -= self.atk
        self.atk += self.atk / 2
        if self.hp >= 0:
            print(self.name, "还有血量", self.hp, "攻击力为", self.atk)
        else:
            print("Game Over, Player has been dead, start a new game if you'd love to!")


class Enemy:
    def __init__(self, name, atk, hp):
        self.name = name
        self.atk = atk
        self.hp = hp

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        self.__atk = value

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value

    def fire_player(self, player):  # 表示袭击了一个敌人
        player.hp -= self.atk
        self.atk += self.atk / 2
        if self.hp >= 0:
            print(self.name, "还有血量", self.hp, "攻击力为", self.atk)
        else:
            print("Game Over, Enemy has been dead! You are the champion !")


p01 = Player(1, 20, 20)
p02 = Player(2, 15, 25)
e01 = Enemy(3, 30, 30)
e02 = Enemy(4, 5, 6)

p01.fire_enemy(e01)
p01.fire_enemy(e02)
e02.fire_player(p02)
