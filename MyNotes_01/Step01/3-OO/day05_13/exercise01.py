# author: Ziming Guo
# time: 2020/2/20
"""
    练习1：
    定义父类
        动物（行为：叫）

    定义子类
        狗（行为：跑）
        鸟（行为：飞）

    创建三个类型的对象
    体会：isinstance(对象,类型)
    体会：issubclass(类型,类型)
"""


class Animal:
    def brood(self):
        print("繁殖")

    def bark(self):
        print("叫")

    def live(self):
        print("活着")


class Dog(Animal):
    def run(self):
        print("跑步")

    def bone(self):
        print("啃骨头")


class Bird(Animal):
    def fly(self):
        print("飞翔")

    def on_the_tree(self):
        print("上树")


a01 = Animal()
d01 = Dog()
b01 = Bird()

# isinstance
print(isinstance(a01, Animal))  # T
print(isinstance(d01, Animal))  # T
print(isinstance(b01, Animal))  # T

print(isinstance(a01, Dog))  # F
print(isinstance(d01, Dog))  # T
print(isinstance(b01, Dog))  # F

print(isinstance(a01, Bird))  # F
print(isinstance(d01, Bird))  # F
print(isinstance(b01, Bird))  # T

# issubclass
print(issubclass(Animal, Animal))  # T
print(issubclass(Dog, Animal))  # T
print(issubclass(Bird, Animal))  # T
print(issubclass(Animal, Dog))  # F
print(issubclass(Animal, Bird))  # F
