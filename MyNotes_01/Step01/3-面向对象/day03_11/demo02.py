# author: Ziming Guo
# time: 2020/2/16
"""
    使用property(读取方法，写入方法)对象,封装变量.
"""
class Wife:
    def __init__(self, name, age, weight):
        self.name = name
        # self.set_age(age)
        self.age = age
        # self.set_weight(weight) # 在下面做这个 set_weight 方法的目的就是
                                  # 为了在设置 weight 的时候做一下逻辑判断 符合传进去 不符合就退出来
        self.weight = weight  # 而这节课讲的就是，不要之前那么包装了
                              # 用新的方法来封装，看上去会更像个变量

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if 21 <= value <= 31:
            self.__age = value
        else:
            raise ValueError("我不要")

    # 属性  property对象拦截对age 类 变量的读写操作
    # 但是读写的都是 __age
    age = property(get_age,set_age) # 就是因为这句话，把下面的变量的行为，拿给方法去做了

    def get_weight(self):
        return self.__weight

    def set_weight(self, value):
        if 40 <= value <= 60:
            self.__weight = value
        else:
            raise ValueError("我不要")
    # 进行拦截（创建了一个类变量）
    weight = property(get_weight,set_weight)

w01 = Wife("铁锤公主", 30, 50)
# w01.set_age(25)
w01.age = 25 # 在写入时执行了写入方法
             # 把 25 写入给了 age ，所以是写入
             # 看上去 25 给到了 age ，但是实际上是给了 __age
print(w01.age) # 在读取时执行了读取方法
               # 看上去是把 age 读了出来，实际上是读了 __age
# 上面这两句话说明：
#      看似是对实例变量进行操作，但是其实没有创建新的变量出来

w01.weight = 45
print(w01.weight)