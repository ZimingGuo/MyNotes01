# author: Ziming Guo
# time: 2020/2/25
'''
    练习4：
    员工管理器记录多个员工
    得带员工管理器对象
    再：画一个设计思想的图（封装 继承 多态）
'''


class Employee:
    pass


class EmployeeManager:
    """
        员工管理器
    """

    def __init__(self):
        self.__list_employee = []

    def add_employee(self, employee):
        self.__list_employee.append(employee)

    def __iter__(self):
        return EmployeeInterator(self.__list_employee)


class EmployeeInterator:
    def __init__(self, outer_list):
        self.__outer_list = outer_list
        self.__index = 0

    def __next__(self):
        if self.__index > len(self.__outer_list) - 1:
            raise StopIteration
        temp = self.__outer_list[self.__index]
        self.__index += 1
        return temp


manager = EmployeeManager()
manager.add_employee(Employee())
manager.add_employee(Employee())
manager.add_employee(Employee())

# for item in manager:
#     print(item)

e01 = manager.__iter__()
# 这样就可以迭代 类 了
# 这句话体现了 多态 的思想

while True:
    try:
        item = e01.__next__()
        print(item)
    except StopIteration:
        break
