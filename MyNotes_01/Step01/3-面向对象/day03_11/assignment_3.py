# author: Ziming Guo
# time: 2020/2/17
'''
    作业3：
    请用面向对象思想，描述以下场景：
    张无忌　教　赵敏　九阳神功
    赵敏　教　张无忌　化妆
    张无忌　上班　挣了　10000
    赵敏　上班　挣了　6000
    思考：变化点是数据的不同还是行为的不同。
'''


# Person 类：

class Person:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def teach(self, person, knowledge):
        print(self.name, "教", person.name, knowledge)

    def earn(self, money):
        print(self.name, "原来有", self.money)
        total_money = self.money + money
        print(self.name, "赚了", money, "ta一共有", total_money)


class Knowledge:
    def __init__(self, knowledge):
        self.knowledge = knowledge

    @property
    def knowledge(self):
        return self.__knowledge

    @knowledge.setter
    def knowledge(self, value):
        self.__knowledge = value


class Money:
    def __init__(self, money):
        self.money = money

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value


p01 = Person("赵敏", 0)
p02 = Person("张无忌", 0)
k01 = Knowledge("九阳神功")
k02 = Knowledge("化妆")
m01 = Money(10000)
m02 = Money(6000)

p01.teach(p02, k01.knowledge)
p02.teach(p01, k01.knowledge)
p01.earn(m01.money)
p02.earn(m02.money)
