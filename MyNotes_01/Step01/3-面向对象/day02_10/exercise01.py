# author: Ziming Guo
# time: 2020/2/14
"""
    练习1：
    参照day06/exercise07.py
        1. 创建学生类
            -- 数据：姓名,年龄,成绩，性别
        　　 -- 行为：在控制台中打印个人信息的方法
        2. 在控制台中循环录入学生信息，如果名称是空字符,退出录入。
        3. 在控制台中输出每个学生信息(调用打印学生类的打印方法)
        4.　打印第一个学生信息
"""


# 我现在在做一个新的类型，这个类型是个抽象的概念
class Student:
    # 数据成员
    def __init__(self, name, age, score, sex, count):
        self.name = name  # 这些数据不是这个方法的局部变量，也就是说不会写在栈帧里面
        # 这些变量是在创建对象的时候写的
        self.age = age
        self.score = score
        self.sex = sex
        self.count = count

    # 行为成员
    def print_self_info(self):
        """
        在控制台中打印个人信息
        """
        print("第%d个学生的姓名是%s,年龄是%s,成绩是%s,性别是%s" %
              (self.count, self.name, self.age, self.score, self.sex))


# 创建对象
# 创建完的对象，通过 self 也能访问
# s01 = Student("赵敏", 26, 100, "女")
# 这是昨天写的，今天不这么干了，今天的这些数据来自于控制台

# 调用行为
# 这个 print_self_info 方法可以通过 self 访问对象的数据
# s01.print_self_info()


list_student_info = []
count = 0
while True:
    # dict_student_info = {}

    name = input("请输入学生姓名：")
    if name == "":
        break
    # dict_student_info["name"] = name

    age = input("请输入学生年龄：")
    if age == "":
        break
    # dict_student_info["age"] = age

    score = input("请输入学生成绩：")
    if score == "":
        break
    # dict_student_info["score"] = score

    sex = input("请输入学生性别：")
    if sex == "":
        break
    # dict_student_info["gender"] = gender

    count += 1  # 表示录入的第几个学生
                # 这个count记录的是这个录入的是第几个学生
    stu = Student(name, age, score, sex, count)  # 创建对象,之后这个对象可以调用之间定义的行为
    list_student_info.append(stu)  # 把创建的对象放进列表
                                   # 列表里面有很多对象，每一个对象都是一个同学，把这些对象放进一个列表里面存储起来
                                   # 在内存图里看，这个列表和原来的列表没有差异
                                   # 只不过列表里的元素所指向的东西不一样了；原来指向变量，现在指向的是个 对象

count01 = -1 # 这个count01表示的是一会在打印的时候，应该打印对象列表里的第几组元素
for stu in list_student_info:  # 这个 stu 里面装的就是学生(对象)
                                # stu 是列表里面的每一个元素，即：对象的地址
    stu.print_self_info()  # 对于列表里的每一个对象，都调用一次 print_self_info 这个函数，用来打印学生的信息

    count01 += 1
    info = list_student_info[count01]  # 这相当于又创建了一个对象
    info.print_self_info()
