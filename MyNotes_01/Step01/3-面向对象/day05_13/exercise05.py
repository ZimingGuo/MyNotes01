# author: Ziming Guo
# time: 2020/2/21
"""
    练习5：
    定义员工管理器
        1.管理所有员工
        2. 计算所有员工工资

    员工：
        程序员：底薪 + 项目分红
        销售：底薪 + 销售额 * 0.05
        软件测试...
        ...

    要求：增加新岗位，员工管理器不变.
"""


class EmployeeController:
    def __init__(self):
        self.__employee_list = []  # 起了一个私有的名字，因为做代码的人(我)觉得不需要别人看见,但是可以用过方法来操作(读写)

    # @property
    # def employee_list(self):
    #     return self.__employee_list
    #  # 这两步是在保护列表
    # @employee_list.setter
    # def employee_list(self, value):
    #     self.__employee_list = value

    def add_employee(self, person):
        if isinstance(person, Employee):  # 这个地方控制继承
            self.__employee_list.append(person)

    def wage_calculate(self):
        for item in self.__employee_list:
            money = item.calculate()
            print(item.name, "的薪水是:", money)


class Employee:
    def __init__(self, min_wage):
        self.min_wage = min_wage

    def calculate(self):
        return self.min_wage
        # raise NotImplementedError()  # 这个地方控制多态


# ---------------------------------------------------------

class Programmer(Employee):
    def __init__(self, min_wage, bonus, name):
        super().__init__(min_wage)
        self.bonus = bonus
        self.name = name

    def calculate(self):
        return self.min_wage + self.bonus
        # 扩展重写的写法：
        # return super().calculate()+self.bonus


class Seller(Employee):
    def __init__(self, min_wage, sales, name):
        super().__init__(min_wage)
        self.sales = sales
        self.name = name

    def calculate(self):
        return self.min_wage + self.sales * 0.05
        # 扩展重写的写法：
        # return super().calculate()+self.sales * 0.05

ec01 = EmployeeController()
e01 = Employee(1000)
# 这句话可以充分体现父类的参数和子类的参数没有丝毫关系
# 只是在继承的时候要写 super 表示是继承过来的参数

p01 = Programmer(1000, 1500, "技术开发人员")
s01 = Seller(1500, 20000, "销售人员")

ec01.add_employee(p01)
ec01.add_employee(s01)

# 既然已经做成了列表，那么字需要一步 wage_calculate 操作就可以计算所有成员的薪水
ec01.wage_calculate()
