# author: Ziming Guo
# time: 2020/2/23
'''
    界面代码
'''

# import model as m
# import bll as c

import model
import bll

class StudentManagerView:
    """
        学生管理器视图
    """

    def __init__(self):
        # self.__manager = c.StudentManagerController()
        self.__manager = bll.StudentManagerController()
        # 想要只创建一个对象，就把这个创建写成实例变量

    def __display_menu(self):
        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修改学生")
        print("5)按照成绩升序显示学生")

    def __select_menu(self):
        item = input("请输入：")
        if item == "1":
            self.__input_student()
        elif item == "2":
            self.__output_student(self.__manager.stu_list)
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()
        elif item == "5":
            self.__output_student_by_score()

    def main(self):
        """
            界面视图入口
        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_student(self):
        name = input("请输入学生姓名:")
        age = int(input("请输入学生年龄:"))
        score = int(input("请输入学生成绩:"))
        # stu = m.StudentModel(name, age, score)
        stu = model.StudentModel(name, age, score)
        self.__manager.add_student(stu)

    def __output_student(self, list_output):
        for item in list_output:
            print("编号:", item.id, "名字:", item.name, "年龄:", item.age, "成绩:", item.score)

    def __delete_student(self):
        num = int(input("请输入所删除学生的编号:"))
        if self.__manager.remove_student(num):
            print("删除成功！")
        else:
            print("失败！")

    def __modify_student(self):
        id = int(input("请输入要修改的学生的编号:"))
        name = input("请输入新的姓名:")
        age = int(input("请输入新的年龄:"))
        score = int(input("请输入新的成绩:"))
        # info = m.StudentModel(name, age, score, id)
        info = model.StudentModel(name, age, score, id)
        if self.__manager.update_student(info):
            print("更改成功！")
        else:
            print("失败！")

    def __output_student_by_score(self):
        self.__manager.order_by_score()
        self.__output_student(self.__manager.stu_list)
