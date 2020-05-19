# author: Ziming Guo
# time: 2020/2/14
'''
    deom01：
'''
class Student:
    # 数据成员
    def __init__(self, name, age, score, sex):
        # 创建实例变量
        self.name = name  # 这句话就是调用 __iinit__ 创建了一个实例变量
                          # 这些数据不是这个方法的局部变量，也就是说不会写在栈帧里面
                          # 这些变量是在创建对象的时候写的
                          # 我的理解：__init__ 函数(方法)的作用就是把对象的里的数据和外面的变量连结起来了
        self.age = age
        self.score = score
        self.sex = sex

    # 行为成员
    def print_self_info(self): # 这个地方有一个参数，但是在实际调用的时候从来不会填写
                               # 因为在调用的时候会自动把对象的地址产地进去
        # 读取实例变量
        print("第个学生的姓名是%s,年龄是%s,成绩是%s,性别是%s" %
              (self.name, self.age, self.score, self.sex)) # 这句话就是在一次次访问(读取)实例变量



list01 = [
    Student("赵敏", 28, 100, "女"), # 这句话就是调用 __init__ 创建了一个对象
                                   # 并把这个创建好的对象放进了一个列表里面
    Student("苏大强", 68, 62, "男")
] # 建立了一个列表，列表里面是创建的两个对象

s01 = list01[0] # 把第一个对象调出来，把地址给了 s01
s01.name = "小赵"
s01.score = 98
print(list01[0].name, list01[0].score)
Student("赵敏", 28, 100, "女").print_self_info()
