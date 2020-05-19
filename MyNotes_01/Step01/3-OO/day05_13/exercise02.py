# author: Ziming Guo
# time: 2020/2/20
"""
    练习2：
    定义父类
        车（数据：品牌,速度）

    定义子类
        电动车（数据：电池容量,充电功率）

    创建两个对象
    画出内存图.
"""


class Car:
    def __init__(self, brand, velocity):
        self.brand = brand
        self.volicity = velocity

    def print_info(self):
        print(self.brand, self.volicity)


class ElectricalCar(Car):
    def __init__(self, brand, velocity, battery_volumn, battery_power):
        super().__init__(brand, velocity)
        self.battery_volumn = battery_volumn
        self.battery_power = battery_power

    def print_info_01(self):
        print(self.brand, self.volicity, self.battery_volumn, self.battery_power)


c01 = Car("BMW", 100)
e01 = ElectricalCar("VW", 90, 1000, 80)

c01.print_info()  # BMW 100
e01.print_info()  # VW 90 # 说明子类可以调父类的方法
e01.print_info_01()  # VW 90 1000 80
